from flask import Flask, request, jsonify, render_template, send_file
import os
import hashlib
import cv2

from database.db import get_db_connection
from core.embed import embed_watermark
from core.extract import extract_watermark
from security.keys import get_secret_key

app = Flask(__name__)

# --------------------------------------------------
# CONSTANTS
# --------------------------------------------------

WATERMARK_LEN = 32          # fixed-length watermark
SIMILARITY_THRESHOLD = 0.90  # 90% match accepted


# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------

def similarity(a: str, b: str) -> float:
    """
    Compute similarity ratio between two equal-length strings
    """
    if len(a) != len(b):
        return 0.0
    matches = sum(x == y for x, y in zip(a, b))
    return matches / len(a)


# --------------------------------------------------
# BASIC ROUTES
# --------------------------------------------------

@app.route("/")
def home():
    return "Traitor-Tracer API is running 🚀"


@app.route("/test-db")
def test_db():
    conn = get_db_connection()
    conn.close()
    return "Supabase DB connected successfully ✅"


# --------------------------------------------------
# SINGLE DASHBOARD UI
# --------------------------------------------------

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/index")
def index():
    return render_template("index.html")

# --------------------------------------------------
# IMAGE UPLOAD + WATERMARK EMBEDDING
# --------------------------------------------------

@app.route("/upload", methods=["POST"])
def upload_image():
    user_id = request.form.get("user_id")
    image = request.files.get("image")

    if not user_id or not image:
        return "Missing user_id or image", 400

    os.makedirs("samples/original", exist_ok=True)
    os.makedirs("samples/watermarked", exist_ok=True)

    input_path = os.path.join("samples/original", image.filename)
    output_path = os.path.join("samples/watermarked", image.filename)

    image.save(input_path)

    # 🔐 FIXED-LENGTH watermark (robust + extractable)
    base_secret = get_secret_key()
    watermark_text = hashlib.sha256(
        f"{base_secret}:{user_id}".encode()
    ).hexdigest()[:WATERMARK_LEN]

    # 🔥 Embed watermark
    watermarked_img = embed_watermark(input_path, watermark_text)
    cv2.imwrite(output_path, watermarked_img)

    # Optional content hash
    content_hash = hashlib.sha256(image.filename.encode()).hexdigest()

    # Store in DB
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO watermark_records (user_id, content_hash, watermark_key)
        VALUES (%s, %s, %s)
        """,
        (user_id, content_hash, watermark_text)
    )
    conn.commit()
    cur.close()
    conn.close()

    return send_file(output_path, as_attachment=True)


# --------------------------------------------------
# TRAITOR CHECK FROM LEAKED IMAGE (ROBUST)
# --------------------------------------------------

@app.route("/trace-image", methods=["POST"])
def trace_image():
    image = request.files.get("image")

    if not image:
        return render_template(
            "dashboard.html",
            error="Please upload an image"
        )

    os.makedirs("samples/attacked", exist_ok=True)

    image_path = os.path.join("samples/attacked", image.filename)
    image.save(image_path)

    try:
        extracted_text = extract_watermark(image_path, WATERMARK_LEN)
        extracted_text = extracted_text.strip()
        print("EXTRACTED:", extracted_text)
    except Exception as e:
        print("Extraction error:", e)
        return render_template(
            "dashboard.html",
            error="Watermark extraction failed"
        )

    # Fetch all watermark records
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT user_id, watermark_key, created_at FROM watermark_records"
    )
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    # Similarity-based matching
    for user_id, stored_key, created_at in rows:
        score = similarity(extracted_text, stored_key)
        print(
            f"COMPARE → extracted={extracted_text} "
            f"stored={stored_key} "
            f"score={score:.2f}"
        )

        if score >= SIMILARITY_THRESHOLD:
            return render_template(
                "dashboard.html",
                result={
                    "user": user_id,
                    "time": str(created_at),
                    "score": f"{score * 100:.1f}%"
                }
            )

    return render_template(
        "dashboard.html",
        error="No traitor found for this image"
    )


# --------------------------------------------------
# RUN APP
# --------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)

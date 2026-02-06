import hashlib
from security.keys import get_secret_key


def hash_watermark(watermark_text: str) -> str:
    """
    Hash watermark with secret salt
    Used for ownership verification
    """
    secret = get_secret_key()
    payload = (watermark_text + secret).encode()

    return hashlib.sha256(payload).hexdigest()

"""
Global configuration settings for Traitor-Tracer
Change values here instead of editing core logic
"""

# ===============================
# Watermark Parameters
# ===============================

# Strength of embedding (higher = more robust, lower = more invisible)
WATERMARK_ALPHA = 5

# DWT wavelet type
DWT_WAVELET = "haar"

# Block size for DCT embedding
BLOCK_SIZE = 8

# Error correction repetition
ECC_REPEAT = 3

# ===============================
# Security
# ===============================

# Secret salt for watermark hashing (change in production)
SECRET_SALT = "traitor_tracer_secret"

# AES key size (if encryption enabled)
AES_KEY_SIZE = 256

# ===============================
# Image Constraints
# ===============================

# Minimum image size to embed watermark
MIN_IMAGE_SIZE = (256, 256)

# Allowed formats
ALLOWED_FORMATS = ["jpg", "jpeg", "png"]

# ===============================
# Extraction
# ===============================

# Detection threshold
DETECTION_THRESHOLD = 0

# ===============================
# Debug / Logging
# ===============================

DEBUG = True
LOG_LEVEL = "INFO"

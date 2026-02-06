import cv2
import numpy as np


def compression_attack(image, quality=30):
    """
    JPEG compression
    quality: 1–100 (lower = stronger attack)
    """
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    _, encimg = cv2.imencode(".jpg", image, encode_param)
    return cv2.imdecode(encimg, cv2.IMREAD_GRAYSCALE)

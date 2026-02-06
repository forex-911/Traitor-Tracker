import cv2
import numpy as np


def crop_attack(image, crop_ratio=0.7):
    """
    Crop the center of the image
    crop_ratio: 0.7 keeps 70% of image
    """
    h, w = image.shape[:2]
    ch, cw = int(h * crop_ratio), int(w * crop_ratio)

    y1 = (h - ch) // 2
    x1 = (w - cw) // 2

    return image[y1:y1 + ch, x1:x1 + cw]

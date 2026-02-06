import cv2
import os


def load_grayscale(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Image not found: {path}")

    return cv2.imread(path, cv2.IMREAD_GRAYSCALE)


def save_image(path, image):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    cv2.imwrite(path, image)

import numpy as np
import cv2
from skimage.metrics import structural_similarity as ssim


def calculate_psnr(original, watermarked):
    return cv2.PSNR(original, watermarked)


def calculate_ssim(original, watermarked):
    score, _ = ssim(original, watermarked, full=True)
    return score

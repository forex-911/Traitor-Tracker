import cv2
import os

from attacks.crop import crop_attack
from attacks.resize import resize_attack
from attacks.compress import compression_attack
from attacks.noise import gaussian_noise

from core.embed import embed_watermark
from core.detect import detect_watermark_energy

ORIGINAL = "samples/original/test.jpg"
WATERMARKED = "samples/watermarked/test.jpg"
ATTACKED_DIR = "samples/attacked"

WATERMARK_TEXT = "TRAITOR"

os.makedirs(ATTACKED_DIR, exist_ok=True)


def ensure_watermarked():
    if not os.path.exists(WATERMARKED):
        wm = embed_watermark(ORIGINAL, WATERMARK_TEXT)
        cv2.imwrite(WATERMARKED, wm)


def assert_detected(path):
    assert detect_watermark_energy(path), "Watermark NOT detected"


def test_crop_attack():
    ensure_watermarked()
    img = cv2.imread(WATERMARKED)

    attacked = crop_attack(img, 0.6)
    path = os.path.join(ATTACKED_DIR, "crop.jpg")
    cv2.imwrite(path, attacked)

    assert_detected(path)


def test_resize_attack():
    ensure_watermarked()
    img = cv2.imread(WATERMARKED)

    attacked = resize_attack(img, 0.5)
    path = os.path.join(ATTACKED_DIR, "resize.jpg")
    cv2.imwrite(path, attacked)

    assert_detected(path)


def test_compression_attack():
    ensure_watermarked()
    img = cv2.imread(WATERMARKED)

    attacked = compression_attack(img, 25)
    path = os.path.join(ATTACKED_DIR, "compress.jpg")
    cv2.imwrite(path, attacked)

    assert_detected(path)


def test_noise_attack():
    ensure_watermarked()
    img = cv2.imread(WATERMARKED)

    attacked = gaussian_noise(img, var=20)
    path = os.path.join(ATTACKED_DIR, "noise.jpg")
    cv2.imwrite(path, attacked)

    assert_detected(path)

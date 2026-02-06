import cv2
import numpy as np
from core.frequency import apply_dwt, apply_dct
from core.redundancy import split_blocks


def detect_watermark_energy(image_path, threshold=0.5):
    """
    Detect watermark presence based on DCT coefficient energy.
    Returns True if watermark is present.
    """
    img = cv2.imread(image_path)
    if img is None:
        return False

    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    Y, _, _ = cv2.split(ycrcb)
    Y = Y.astype(np.float32)

    _, (LH, _, _) = apply_dwt(Y)

    blocks = split_blocks(LH)
    values = []

    for _, _, block in blocks:
        dct_block = apply_dct(block)
        values.append(abs(dct_block[4, 4]))

    if not values:
        return False

    # Normalize energy
    energy = np.mean(values)
    return energy > threshold

import cv2
import numpy as np

from core.frequency import apply_dwt, inverse_dwt, apply_dct, inverse_dct
from core.redundancy import split_blocks, merge_blocks
from core.error_correction import encode_bits
from config.settings import WATERMARK_ALPHA


def embed_watermark(image_path, watermark_text):
    # 1️⃣ Read color image
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Image not found or invalid format")

    # 2️⃣ Convert to YCrCb
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    Y, Cr, Cb = cv2.split(ycrcb)

    Y = Y.astype(np.float32)

    # 3️⃣ DWT on luminance
    LL, (LH, HL, HH) = apply_dwt(Y)

    # 4️⃣ Watermark → bits + redundancy
    bits = [int(b) for b in ''.join(format(ord(c), '08b') for c in watermark_text)]
    bits = encode_bits(bits)

    # 5️⃣ Embed in DCT blocks
    blocks = split_blocks(LH)
    bit_index = 0
    new_blocks = []

    for y, x, block in blocks:
        if bit_index >= len(bits):
            new_blocks.append((y, x, block))
            continue

        dct_block = apply_dct(block)
        dct_block[4, 4] += WATERMARK_ALPHA if bits[bit_index] else -WATERMARK_ALPHA
        bit_index += 1

        new_blocks.append((y, x, inverse_dct(dct_block)))

    LH = merge_blocks(LH, new_blocks)

    # 6️⃣ Inverse DWT
    Y_wm = inverse_dwt((LL, (LH, HL, HH)))

    # 🔧 CRITICAL FIX: restore original size
    Y_wm = cv2.resize(Y_wm, (Y.shape[1], Y.shape[0]))

    Y_wm = np.clip(Y_wm, 0, 255).astype(np.uint8)

    # 7️⃣ Merge channels safely
    Cr = cv2.resize(Cr, (Y.shape[1], Y.shape[0]))
    Cb = cv2.resize(Cb, (Y.shape[1], Y.shape[0]))

    ycrcb_wm = cv2.merge([Y_wm, Cr, Cb])
    final_img = cv2.cvtColor(ycrcb_wm, cv2.COLOR_YCrCb2BGR)

    return final_img

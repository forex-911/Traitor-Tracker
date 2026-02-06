import cv2
import os
from core.embed import embed_watermark

INPUT_IMAGE = "samples/original/test.jpg"
OUTPUT_IMAGE = "samples/watermarked/test_wm.jpg"


def test_embed_watermark():
    assert os.path.exists(INPUT_IMAGE), "Input image missing"

    wm_image = embed_watermark(INPUT_IMAGE, "TRAITOR")

    cv2.imwrite(OUTPUT_IMAGE, wm_image)

    assert os.path.exists(OUTPUT_IMAGE)
    assert wm_image is not None

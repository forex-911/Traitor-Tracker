from core.extract import extract_watermark

WATERMARKED_IMAGE = "samples/watermarked/test_wm.jpg"


def test_extract_watermark():
    extracted = extract_watermark(WATERMARKED_IMAGE, length=7)
    assert "TRAITOR" in extracted

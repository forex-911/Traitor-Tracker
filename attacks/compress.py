import cv2


def run(image_path: str) -> str:
    image = cv2.imread(image_path)

    out_path = image_path.replace(".", "_jpeg.")
    cv2.imwrite(out_path, image, [cv2.IMWRITE_JPEG_QUALITY, 30])

    return out_path
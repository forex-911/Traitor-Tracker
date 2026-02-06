import cv2


def run(image_path: str) -> str:
    image = cv2.imread(image_path)

    # Scale down to 50%
    resized = cv2.resize(image, None, fx=0.5, fy=0.5)

    out_path = image_path.replace(".", "_resize.")
    cv2.imwrite(out_path, resized)
    return out_path
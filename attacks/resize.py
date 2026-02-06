import cv2


def resize_attack(image, scale=0.5):
    """
    Resize image down and back up
    scale < 1 reduces image size
    """
    h, w = image.shape[:2]

    resized = cv2.resize(image, None, fx=scale, fy=scale,
                          interpolation=cv2.INTER_LINEAR)

    restored = cv2.resize(resized, (w, h),
                           interpolation=cv2.INTER_LINEAR)

    return restored

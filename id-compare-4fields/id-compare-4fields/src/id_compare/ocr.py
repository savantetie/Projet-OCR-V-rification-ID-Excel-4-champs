import cv2, pytesseract

def read_text(img_path: str, lang: str = "fra") -> str:
    """Read text from an ID image with simple binarization before OCR."""
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Image not found: {img_path}")
    _, bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    cfg = "--oem 3 --psm 6"
    return pytesseract.image_to_string(bw, lang=lang, config=cfg)

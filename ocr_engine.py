import easyocr
import numpy as np

# English OCR reader
reader = easyocr.Reader(['en'], gpu=False)


def extract_text(image):
    """
    Extract text from prescription image.
    """

    # PIL image → NumPy array
    image_array = np.array(image)

    # OCR
    results = reader.readtext(image_array)

    extracted_text = []

    for _, text, confidence in results:
        if confidence > 0.30:
            extracted_text.append(text)

    return "\n".join(extracted_text)

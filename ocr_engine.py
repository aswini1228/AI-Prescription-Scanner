import easyocr
import numpy as np

reader = None


def extract_text(image):

    global reader

    if reader is None:
        reader = easyocr.Reader(['en'], gpu=False)

    image_array = np.array(image)

    results = reader.readtext(image_array)

    extracted_text = []

    for _, text, confidence in results:
        if confidence > 0.30:
            extracted_text.append(text)

    return "\n".join(extracted_text)

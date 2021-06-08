import pytesseract
from googletrans import Translator


def translate(image, lang='rus'):
    result = pytesseract.image_to_string(image, lang=lang)
    gt = Translator()
    string_translated = gt.translate(result)
    return str(string_translated.text)


import re
from pyarabic.araby import strip_tashkeel, normalize_hamza
def clean_arabic_text(text):
    """
    Cleans and normalizes Arabic text for classification models.
    Removes diacritics, digits, English characters, and normalizes Arabic letters.
    """
    # Remove diacritics
    text = strip_tashkeel(text)

    # Normalize Alef variants to bare Alef
    text = re.sub(r"[إأآ]", "ا", text)

    # Replace final Yeh (ى) with standard Yeh (ي)
    text = re.sub(r"ى", "ي", text)

    # Replace Teh Marbuta with Heh
    text = re.sub(r"ة", "ه", text)

    # Normalize Waw Hamza and Yeh Hamza to Waw/Yeh (اختياري)
    text = re.sub(r"ؤ", "و", text)
    text = re.sub(r"ئ", "ي", text)

    # Remove standalone Hamza (ء) if not inside word
    text = re.sub(r"\bء\b", "", text)

    # Remove digits (Arabic and English)
    text = re.sub(r"[0-9٠-٩]", "", text)

    # Remove English letters and special characters
    text = re.sub(r"[a-zA-Z@#%^&*()_+=\[{\]};:<>|./~`!\"؟،]", " ", text)

    # Remove multiple spaces and newlines
    text = re.sub(r"\s+", " ", text).strip()

    return text

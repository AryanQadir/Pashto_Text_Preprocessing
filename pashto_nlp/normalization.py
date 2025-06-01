import re
import unicodedata

def normalize_text(text: str) -> str:
    """
    Normalize Pashto text by applying:
    - Unicode NFC normalization
    - Standardizing Arabic characters to Pashto variants
    - Removing diacritics (optional: can keep if you want)
    - Fixing spacing
    - Removing unwanted symbols
    
    Args:
        text (str): Raw Pashto text.
        
    Returns:
        str: Normalized Pashto text.
    """
    if not text:
        return ""
    
    # Step 1: Unicode normalization (NFC)
    text = unicodedata.normalize('NFC', text)
    
    # Step 2: Normalize Arabic characters to Pashto
    text = text.replace('ك', 'ک')
    text = text.replace('ي', 'ی')
    
    # Step 3: Remove Arabic diacritics (Tashdid, Sukun, etc.)
    arabic_diacritics = re.compile(r'[\u064B-\u065F\u0670\u06D6-\u06ED]')
    text = arabic_diacritics.sub('', text)
    
    # Step 4: Normalize Hamza forms if needed
    text = text.replace('أ', 'ا').replace('إ', 'ا').replace('آ', 'ا')
    
    # Step 5: Remove tatweel (kashida) — elongation character
    text = text.replace('ـ', '')
    
    # Step 6: Remove any non-Pashto alphabet characters except spaces and basic punctuation
    allowed_chars_pattern = re.compile(r'[^ء-ي۰-۹-،؛؟ٔء-ی\s\.,!?]')
    text = allowed_chars_pattern.sub('', text)
    
    # Step 7: Fix multiple spaces into one
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

if __name__ == "__main__":
    sample_text = "آيا كابل يوازې يو ښار دی؟"
    print("Original:", sample_text)
    print("Normalized:", normalize_text(sample_text))

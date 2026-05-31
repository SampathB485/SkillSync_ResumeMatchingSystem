import re


def clean_text(text):
    """Clean text for NLP processing."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def preprocess_text(text):
    """
    Preprocess text for analysis and matching.
    
    Args:
        text (str): Raw text to preprocess
        
    Returns:
        str: Cleaned and normalized text
    """
    if not text or not isinstance(text, str):
        return ""
    
    return clean_text(text)

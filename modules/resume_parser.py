"""Resume parser - extracts and structures resume information."""
from nlp.text_preprocessor import preprocess_text
from nlp.skill_extractor import extract_skills


def parse_resume(path):
    """
    Parse resume text and return structured representation.
    
    Args:
        path (str): Raw resume text or path
        
    Returns:
        dict: Structured resume data with skills, experience, etc.
    """
    if not path or not isinstance(path, str):
        return {
            "text": "",
            "processed_text": "",
            "skills": [],
            "keywords": [],
            "word_count": 0
        }
    
    text = path  # In this context, path is actually the resume text
    processed_text = preprocess_text(text)
    skills = extract_skills(text)
    
    # Extract key terms (high frequency words)
    words = processed_text.split()
    word_count = len(words)
    
    # Basic keyword extraction (words with 5+ characters)
    keywords = list(set([w for w in words if len(w) >= 5]))[:10]
    
    return {
        "text": text,
        "processed_text": processed_text,
        "skills": skills,
        "keywords": keywords,
        "word_count": word_count
    }

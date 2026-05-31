"""Job description analyzer - extracts and structures job information."""
from nlp.text_preprocessor import preprocess_text
from nlp.skill_extractor import extract_skills


def analyze_job_description(text):
    """
    Analyze job description and return structured representation.
    
    Args:
        text (str): Raw job description text
        
    Returns:
        dict: Structured job data with title, skills, and other info
    """
    if not text or not isinstance(text, str):
        return {
            "text": "",
            "processed_text": "",
            "skills": [],
            "keywords": [],
            "word_count": 0
        }
    
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

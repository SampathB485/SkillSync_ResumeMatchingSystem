"""Job description parser - processes and extracts job information."""
from nlp.text_preprocessor import preprocess_text
from nlp.skill_extractor import extract_skills


def parse_job_description(text):
    """
    Parse and normalize job description text.
    
    Args:
        text (str): Raw job description text
        
    Returns:
        dict: Parsed job data with normalized text and extracted skills
    """
    if not text or not isinstance(text, str):
        return {
            "text": "",
            "processed_text": "",
            "skills": []
        }
    
    # Process the text
    processed_text = preprocess_text(text)
    
    # Extract skills from the job description
    skills = extract_skills(text)
    
    return {
        "text": text,
        "processed_text": processed_text,
        "skills": skills
    }

"""Skill extractor - wrapper around NLP skill extraction."""
from nlp.skill_extractor import extract_skills as nlp_extract_skills


def extract_skills(text):
    """
    Extract skills from text using NLP module.
    
    Args:
        text (str): Text to extract skills from
        
    Returns:
        list: List of extracted skills
    """
    if not text or not isinstance(text, str):
        return []
    
    return nlp_extract_skills(text)

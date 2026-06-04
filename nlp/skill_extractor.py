import json
from pathlib import Path
from difflib import SequenceMatcher

SKILLS_FILE = Path(__file__).resolve().parent.parent / "models" / "skills_dictionary.json"

# Common skill abbreviations mapping
SKILL_ABBREVIATIONS = {
    "ml": "machine learning",
    "ai": "artificial intelligence",
    "nlp": "nlp",
    "cv": "computer vision",
    "dl": "deep learning",
    "rnn": "recurrent neural network",
    "cnn": "convolutional neural network",
    "gcp": "google cloud",
    "aws": "aws",
    "ci/cd": "ci cd",
    "rest": "rest api",
    "crud": "crud",
}


def _fuzzy_match(text, skill, threshold=0.8):
    """
    Check if text contains a fuzzy match of skill.
    
    Args:
        text (str): Text to search in
        skill (str): Skill to match
        threshold (float): Minimum similarity ratio (0-1)
        
    Returns:
        bool: True if fuzzy match found
    """
    text_lower = text.lower()
    skill_lower = skill.lower()
    
    # Exact substring match first
    if skill_lower in text_lower:
        return True
    
    # Fuzzy matching on individual words
    words = text_lower.split()
    for word in words:
        ratio = SequenceMatcher(None, skill_lower, word).ratio()
        if ratio >= threshold:
            return True
    
    return False


def extract_skills(text):
    """
    Extract skills from text using intelligent matching.
    Supports exact matching, fuzzy matching, abbreviations, and compound terms.
    
    Args:
        text (str): Text to extract skills from
        
    Returns:
        list: List of extracted skills (deduplicated)
    """
    skills = []
    try:
        with open(SKILLS_FILE, "r", encoding="utf-8") as f:
            skill_dict_data = json.load(f)
    except FileNotFoundError:
        skill_dict_data = {}

    # Flatten the skills dictionary - handle both dict and list formats
    all_skills = []
    if isinstance(skill_dict_data, dict):
        # If it's a dictionary with categories, flatten it
        for category, skill_list in skill_dict_data.items():
            if isinstance(skill_list, list):
                all_skills.extend(skill_list)
    elif isinstance(skill_dict_data, list):
        # If it's already a list, use it directly
        all_skills = skill_dict_data

    if not text or not isinstance(text, str):
        return []

    # Process abbreviations first
    text_expanded = text
    for abbrev, full_form in SKILL_ABBREVIATIONS.items():
        text_expanded = text_expanded.lower().replace(abbrev.lower(), full_form + " ")

    # Extract skills using multiple strategies
    matched_skills = set()
    normalized_text = text_expanded.lower()
    
    for skill in all_skills:
        if isinstance(skill, str):
            skill_lower = skill.lower()
            
            # Strategy 1: Exact substring match
            if skill_lower in normalized_text:
                matched_skills.add(skill)
            
            # Strategy 2: Fuzzy match for longer skills (5+ chars)
            elif len(skill) >= 5:
                if _fuzzy_match(text_expanded, skill, threshold=0.85):
                    matched_skills.add(skill)
    
    return sorted(list(matched_skills))

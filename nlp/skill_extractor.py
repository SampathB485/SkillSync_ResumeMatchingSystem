import json
from pathlib import Path

SKILLS_FILE = Path(__file__).resolve().parent.parent / "models" / "skills_dictionary.json"


def extract_skills(text):
    """Extract skills from text using a simple keyword dictionary."""
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

    normalized = text.lower()
    for skill in all_skills:
        if isinstance(skill, str) and skill.lower() in normalized:
            skills.append(skill)
    
    return list(set(skills))

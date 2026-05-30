import json
from pathlib import Path

SKILLS_FILE = Path(__file__).resolve().parent.parent / "models" / "skills_dictionary.json"


def extract_skills(text):
    """Extract skills from text using a simple keyword dictionary."""
    skills = []
    try:
        with open(SKILLS_FILE, "r", encoding="utf-8") as f:
            skill_dict = json.load(f)
    except FileNotFoundError:
        skill_dict = []

    normalized = text.lower()
    for skill in skill_dict:
        if skill.lower() in normalized:
            skills.append(skill)
    return list(set(skills))

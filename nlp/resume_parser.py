import os


def parse_resume(file_path):
    """Parse resume file and return extracted plain text."""
    if not os.path.exists(file_path):
        return ""
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

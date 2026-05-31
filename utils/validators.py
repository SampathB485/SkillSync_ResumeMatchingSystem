import re


def validate_email(email):
    """
    Validate email format.
    
    Args:
        email (str): Email address to validate
        
    Returns:
        bool: True if valid email format
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validate_password(password):
    """
    Validate password strength.
    
    Args:
        password (str): Password to validate
        
    Returns:
        bool: True if password is at least 6 characters
    """
    return len(password) >= 6


def validate_job_input(job_title, job_description, required_skills):
    """
    Validate job creation inputs.
    
    Args:
        job_title (str): Job title
        job_description (str): Job description
        required_skills (str): Comma-separated list of skills
        
    Returns:
        tuple: (is_valid: bool, message: str)
    """
    # Check if inputs are not empty
    if not job_title or not job_title.strip():
        return False, "Job Title is required."
    
    if not job_description or not job_description.strip():
        return False, "Job Description is required."
    
    if not required_skills or not required_skills.strip():
        return False, "Required Skills are required."
    
    # Check minimum lengths
    if len(job_title.strip()) < 3:
        return False, "Job Title must be at least 3 characters."
    
    if len(job_description.strip()) < 20:
        return False, "Job Description must be at least 20 characters."
    
    # Check maximum lengths
    if len(job_title.strip()) > 200:
        return False, "Job Title cannot exceed 200 characters."
    
    if len(job_description.strip()) > 5000:
        return False, "Job Description cannot exceed 5000 characters."
    
    if len(required_skills.strip()) > 500:
        return False, "Required Skills cannot exceed 500 characters."
    
    return True, "Validation passed."


def validate_resume_upload(filename, file_size):
    """
    Validate resume file before upload.
    
    Args:
        filename (str): Name of the file
        file_size (int): Size of the file in bytes
        
    Returns:
        tuple: (is_valid: bool, message: str)
    """
    # Check file extension
    allowed_extensions = {'.pdf', '.txt', '.doc', '.docx'}
    file_ext = ''.join(list(filename)[-4:]).lower()
    
    if not any(file_ext.endswith(ext) for ext in allowed_extensions):
        return False, "Only PDF, TXT, DOC, and DOCX files are allowed."
    
    # Check file size (max 10MB)
    max_size = 10 * 1024 * 1024
    if file_size > max_size:
        return False, f"File size exceeds maximum limit of 10MB."
    
    return True, "File validation passed."
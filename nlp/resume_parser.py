import os
import pdfplumber


def _extract_text_from_pdf(pdf_path):
    """Extract text from PDF file using pdfplumber."""
    try:
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
    except Exception as e:
        print(f"Error extracting PDF: {str(e)}")
        return ""


def _extract_text_from_file(file_path):
    """Extract text from plain text files (txt, doc, docx)."""
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return ""


def parse_resume(file_path):
    """
    Parse resume file and return extracted plain text.
    Supports PDF, TXT, DOC, and DOCX formats.
    
    Args:
        file_path (str): Path to the resume file
        
    Returns:
        str: Extracted text from the resume
    """
    if not os.path.exists(file_path):
        return ""
    
    # Detect file type by extension
    file_ext = os.path.splitext(file_path)[1].lower()
    
    if file_ext == ".pdf":
        return _extract_text_from_pdf(file_path)
    else:
        # For txt, doc, docx, or other text-based formats
        return _extract_text_from_file(file_path)

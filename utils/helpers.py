"""Utility helper functions."""

def read_text_file(path):
    """Read and return text file contents."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_text_file(path, content):
    """Write text content to a file."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

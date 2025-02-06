import os

def read_file(file_path: str) -> str:
    """Read content from a file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def write_file(file_path: str, content: str):
    """Write content to a file."""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

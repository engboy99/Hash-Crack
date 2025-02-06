import os
from .core import generate_hash

def scan_directory(directory_path: str, algorithm: str = "sha256"):
    """Scan all files in a directory and compute their hashes."""
    file_hashes = {}
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory not found: {directory_path}")
    
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "rb") as f:
                    data = f.read()
                    file_hashes[file_path] = generate_hash(data.decode("utf-8", errors="ignore"), algorithm)
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

    return file_hashes

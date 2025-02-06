import re

HASH_PATTERNS = {
    "md5": r"^[a-f0-9]{32}$",
    "sha1": r"^[a-f0-9]{40}$",
    "sha256": r"^[a-f0-9]{64}$",
    "sha512": r"^[a-f0-9]{128}$"
}

def detect_hash_type(hash_value: str):
    """Detect the type of a given hash based on its length and pattern."""
    for hash_type, pattern in HASH_PATTERNS.items():
        if re.match(pattern, hash_value):
            return hash_type
    return "unknown"

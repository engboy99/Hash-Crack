import os

def load_wordlist(wordlist_path: str):
    """Load wordlist for cracking hashes."""
    if not os.path.exists(wordlist_path):
        raise FileNotFoundError("Wordlist file not found.")
    with open(wordlist_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

def crack_hash(hash_value: str, hash_function, wordlist_path: str):
    """Attempt to crack a hash using a wordlist."""
    wordlist = load_wordlist(wordlist_path)
    for word in wordlist:
        if hash_function(word) == hash_value:
            return word
    return None

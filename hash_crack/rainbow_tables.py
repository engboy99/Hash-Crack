RAINBOW_TABLE = {}

def build_rainbow_table(wordlist):
    """Precompute hashes for a given wordlist."""
    global RAINBOW_TABLE
    RAINBOW_TABLE = {word: generate_hash(word) for word in wordlist}

def lookup_rainbow_table(hash_value):
    """Check if a hash exists in the rainbow table."""
    return next((word for word, h in RAINBOW_TABLE.items() if h == hash_value), None)

import hashlib

SUPPORTED_HASHES = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256,
    "sha512": hashlib.sha512
}

def generate_hash(data: str, algorithm: str = "sha256") -> str:
    """Generate a hash of the input data using the specified algorithm."""
    if algorithm not in SUPPORTED_HASHES:
        raise ValueError(f"Unsupported hash algorithm: {algorithm}")
    hash_obj = SUPPORTED_HASHES[algorithm]()
    hash_obj.update(data.encode())
    return hash_obj.hexdigest()

def verify_hash(data: str, hash_value: str, algorithm: str = "sha256") -> bool:
    """Verify if the given hash matches the input data."""
    return generate_hash(data, algorithm) == hash_value

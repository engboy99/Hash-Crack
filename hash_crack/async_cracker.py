import asyncio

async def async_crack(hash_value, hash_function, wordlist):
    """Asynchronously crack a hash using a wordlist."""
    for word in wordlist:
        if hash_function(word) == hash_value:
            return word
    return None

async def crack_multiple_hashes(hashes, hash_function, wordlist):
    """Crack multiple hashes concurrently."""
    tasks = [async_crack(h, hash_function, wordlist) for h in hashes]
    results = await asyncio.gather(*tasks)
    return results

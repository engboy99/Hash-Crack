import requests

HASH_API_URL = "https://api.hashlookup.com/search"

def query_online_db(hash_value: str):
    """Query an online hash database for matches."""
    response = requests.get(HASH_API_URL, params={"hash": hash_value})
    if response.status_code == 200:
        return response.json()
    return None

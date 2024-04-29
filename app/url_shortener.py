import secrets
from app.models import URLStorage

def shorten_url(url: str, url_storage: URLStorage) -> str:
    """
    Function to shorten a given URL.
    """
    if existing_short_url := url_storage.get_short_url(url):
        return existing_short_url
    
    short_url = generate_short_url()
    url_storage.add_url_mapping(short_url, url)
    return short_url

def generate_short_url() -> str:
    """
    Function to generate a random short URL.
    """
    return secrets.token_urlsafe(6)

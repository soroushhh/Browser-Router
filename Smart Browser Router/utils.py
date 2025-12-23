from urllib.parse import urlparse

def extract_hostname(url: str) -> str:
    if not url.startswith(("http://", "https://")):
        url = "http://" + url
    return urlparse(url).hostname or ""

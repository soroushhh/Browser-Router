from urllib.parse import urlparse, quote_plus

SEARCH_ENGINE = "https://www.google.com/search?q="

def is_probable_domain(raw: str) -> bool:
    return "." in raw and " " not in raw

def normalize_input(raw: str) -> str:
    raw = raw.strip()

    if is_probable_domain(raw):
        if not raw.startswith(("http://", "https://")):
            return "https://" + raw
        return raw

    return SEARCH_ENGINE + quote_plus(raw)

def extract_hostname(url: str) -> str:
    try:
        return urlparse(url).hostname or ""
    except Exception:
        return ""


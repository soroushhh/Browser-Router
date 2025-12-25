import urllib.parse


def normalize_input(text: str) -> str:
    if "://" in text:
        return text

    if "." in text:
        return "https://" + text

    query = urllib.parse.quote_plus(text)
    return f"https://www.google.com/search?q={query}"



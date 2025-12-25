import socket
from urllib.parse import urlparse


def is_reachable(url: str, timeout=2) -> bool:
    parsed = urlparse(url)
    host = parsed.hostname
    port = 443 if parsed.scheme == "https" else 80

    try:
        socket.create_connection((host, port), timeout=timeout)
        return True
    except OSError:
        return False


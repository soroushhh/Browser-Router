import socket

def is_reachable_locally(host: str, timeout: float = 0.5) -> bool:
    try:
        socket.create_connection((host, 443), timeout=timeout)
        return True
    except OSError:
        return False


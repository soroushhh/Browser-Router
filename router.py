from utils import extract_hostname
from network import is_reachable_locally

def choose_profile(url: str) -> str:
    host = extract_hostname(url)

    if not host:
        return "vpn"

    if is_reachable_locally(host):
        return "no_vpn"

    return "vpn"

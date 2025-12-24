from utils import normalize_input, extract_hostname
from network import is_reachable_locally
from cache import get_cached_profile, set_cached_profile

def decide_profile(raw_input: str) -> tuple[str, str]:
    url = normalize_input(raw_input)
    host = extract_hostname(url)

    if not host:
        return url, "vpn"

    cached = get_cached_profile(host)
    if cached:
        return url, cached

    if is_reachable_locally(host):
        set_cached_profile(host, "no_vpn")
        return url, "no_vpn"

    set_cached_profile(host, "vpn")
    return url, "vpn"


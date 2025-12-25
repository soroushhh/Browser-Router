from network import is_reachable
from cache import get_cached_route, set_cached_route


def decide_profile(url: str) -> str:
    cached = get_cached_route(url)
    if cached:
        return cached

    reachable = is_reachable(url)
    profile = "no_vpn" if reachable else "vpn"

    set_cached_route(url, profile)
    return profile


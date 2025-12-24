import json
import os
import time

CACHE_TTL = 6 * 60 * 60
CACHE_FILE = os.path.join(os.path.dirname(__file__), "route_cache.json")

_cache = {}

def load_cache():
    global _cache
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r") as f:
                _cache = json.load(f)
        except Exception:
            _cache = {}

def save_cache():
    try:
        with open(CACHE_FILE, "w") as f:
            json.dump(_cache, f)
    except Exception:
        pass

def get_cached_profile(hostname: str):
    entry = _cache.get(hostname)
    if not entry:
        return None

    if time.time() - entry["ts"] > CACHE_TTL:
        _cache.pop(hostname, None)
        return None

    return entry["profile"]

def set_cached_profile(hostname: str, profile: str):
    _cache[hostname] = {
        "profile": profile,
        "ts": time.time()
    }
    save_cache()

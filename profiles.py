import os
from config import USER_DATA_DIR

def list_chrome_profiles() -> list[str]:
    if not os.path.isdir(USER_DATA_DIR):
        return []

    return [
        d for d in os.listdir(USER_DATA_DIR)
        if os.path.isdir(os.path.join(USER_DATA_DIR, d))
        and (d == "Default" or d.startswith("Profile "))
    ]

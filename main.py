import sys
import os

from utils import normalize_input
from decision import decide_profile
from launcher import launch_chrome


def strip_custom_protocol(arg: str) -> str:
    """
    Windows may pass URLs as:
    smartbrowser://https://example.com
    """
    if arg.startswith("smartbrowser://"):
        return arg[len("smartbrowser://"):]
    return arg


def get_user_input() -> str:
    """
    Collect input passed by Windows or CLI.
    """
    if len(sys.argv) < 2:
        return ""

    raw = sys.argv[1].strip()
    return strip_custom_protocol(raw)


def main():
    user_input = get_user_input()

    # If nothing was passed, open a blank tab safely
    if not user_input:
        launch_chrome("https://www.google.com", profile_type="no_vpn")
        return

    # Normalize input (search vs domain vs URL)
    url = normalize_input(user_input)

    # Decide routing (vpn / no_vpn)
    profile_type = decide_profile(url)

    # Launch Chrome with correct profile
    launch_chrome(url, profile_type=profile_type)


if __name__ == "__main__":
    main()

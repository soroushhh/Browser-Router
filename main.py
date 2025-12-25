import sys

from utils import normalize_input
from decision import decide_profile
from launcher import launch_chrome


def strip_custom_protocol(arg: str) -> str:
    if arg.startswith("smartbrowser://"):
        return arg[len("smartbrowser://"):]
    return arg


def get_user_input() -> str:
    if len(sys.argv) < 2:
        return ""
    return strip_custom_protocol(sys.argv[1].strip())


def main():
    user_input = get_user_input()

    if not user_input:
        launch_chrome("https://www.google.com", profile_key="no_vpn")
        return

    url = normalize_input(user_input)
    profile_key = decide_profile(url)

    launch_chrome(url, profile_key=profile_key)


if __name__ == "__main__":
    main()

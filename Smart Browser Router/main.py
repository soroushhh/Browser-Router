import sys
from router import choose_profile
from launcher import open_in_chrome
from logger import logger

def main():
    if len(sys.argv) < 2:
        logger.warning("No URL provided")
        return

    url = sys.argv[1]
    profile = choose_profile(url)

    logger.info(f"Opening {url} with profile: {profile}")
    open_in_chrome(url, profile)

if __name__ == "__main__":
    main()

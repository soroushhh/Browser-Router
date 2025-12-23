import sys
from router import choose_profile
from launcher import open_in_chrome

def main():
    if len(sys.argv) < 2:
        return

    url = sys.argv[1]
    profile = choose_profile(url)
    open_in_chrome(url, profile)

if __name__ == "__main__":
    main()

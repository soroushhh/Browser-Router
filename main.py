import sys
from cache import load_cache
from decision import decide_profile
from launcher import launch_chrome

def main():
    load_cache()

    if len(sys.argv) < 2:
        print("Usage: smartbrowser <url or search>")
        return

    raw_input = sys.argv[1]
    url, profile = decide_profile(raw_input)

    launch_chrome(url, profile)

if __name__ == "__main__":
    main()

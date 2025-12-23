import subprocess
from config import CHROME_PATH, PROFILES

def open_in_chrome(url: str, profile_key: str):
    subprocess.Popen([
        CHROME_PATH,
        f"--profile-directory={PROFILES[profile_key]}",
        url
    ])

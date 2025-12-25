import os
import subprocess
from config import PROFILES, CHROME_PATH, USER_DATA_DIR


def launch_chrome(url: str, profile_key: str):
    profile_dir = PROFILES[profile_key]

    subprocess.Popen([
        CHROME_PATH,
        f"--user-data-dir={USER_DATA_DIR}",
        f"--profile-directory={profile_dir}",
        url
    ])


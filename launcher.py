import subprocess
from config import CHROME_PATH, USER_DATA_DIR, PROFILES

def launch_chrome(url: str, profile_key: str) -> None:
    profile_dir = PROFILES.get(profile_key)

    if not profile_dir:
        raise ValueError(f"Unknown profile: {profile_key}")

    subprocess.Popen([
        CHROME_PATH,
        f"--user-data-dir={USER_DATA_DIR}",
        f"--profile-directory={profile_dir}",
        url
    ])

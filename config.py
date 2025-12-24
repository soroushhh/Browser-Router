import os

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

USER_DATA_DIR = os.path.join(
    os.environ["LOCALAPPDATA"],
    "Google",
    "Chrome",
    "User Data"
)

PROFILES = {
    "vpn": "Default",
    "no_vpn": "Profile 2"
}


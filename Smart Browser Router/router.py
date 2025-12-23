from config import TLD_NO_VPN, FORCE_NO_VPN, FORCE_VPN
from utils import extract_hostname

def choose_profile(url: str) -> str:
    host = extract_hostname(url).lower()

    if host in FORCE_NO_VPN:
        return "no_vpn"

    if host in FORCE_VPN:
        return "vpn"

    for tld in TLD_NO_VPN:
        if host.endswith(tld):
            return "no_vpn"

    return "vpn"

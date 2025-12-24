SmartBrowser

SmartBrowser is a lightweight Windows tool that automatically opens websites in the correct Chrome profile (VPN or No-VPN) based on real network reachability. Designed for environments with restricted access or network blocks (e.g., in Iran), it intelligently routes traffic without hardcoding domains.

🌟 Features

Automatic routing

Blocked sites → VPN profile

Local sites → No-VPN profile

Network-aware

Real TCP reachability test

No static domain lists

Chrome profile support

Keeps Google account, passwords, bookmarks, and extensions

Fast & cached

Routing decisions cached with TTL for instant performance

Search-friendly

Single words → Google search

Domains → direct navigation

Windows integration

Can be set as the default browser

Safe & reversible

No Chrome hacks, no cookie sharing, no registry changes

🧠 How It Works
User clicks a link
        ↓
SmartBrowser.exe
        ↓
Normalize input (URL or search)
        ↓
Check cache
        ↓
Network reachability test
        ↓
Decide profile: VPN or No-VPN
        ↓
Launch Chrome with correct profile

📂 Project Structure
smart_browser/
├── main.py            # Entry point
├── config.py          # Chrome & profile configuration
├── utils.py           # Input normalization
├── network.py         # Network reachability test
├── decision.py        # Routing decision engine
├── launcher.py        # Chrome launcher
├── cache.py           # Routing cache
├── profiles.py        # Profile discovery helper
├── route_cache.json   # Runtime cache (ignored by git)
├── README.md          # This file

⚙️ Requirements

Python 3.10+ (for development)

Windows 10+

Google Chrome with two profiles:

One with VPN extension enabled

One without VPN extension

🔧 Configuration

config.py example:

PROFILES = {
    "vpn": "Profile 2",
    "no_vpn": "Default"
}


⚠️ Folder names must match Chrome’s actual profile folders (e.g., Default, Profile 2).
Use profiles.py to list existing profiles programmatically.

▶️ Usage (Development)
python main.py github.com
python main.py example.ir
python main.py google


Behavior:

Input	Outcome
github.com	VPN profile (blocked site)
example.ir	No-VPN profile (local site)
google	Google search
📦 Build EXE (Production)
pip install pyinstaller
pyinstaller --onefile --noconsole main.py


Output:

dist/SmartBrowser.exe


Move it to a permanent location:

C:\SmartBrowser\SmartBrowser.exe

🌍 Set as Default Browser (Windows)

Open Settings → Apps → Default Apps

Scroll to Choose defaults by application

Select SmartBrowser

Assign for:

HTTP

HTTPS

.htm

.html

All links now route automatically through SmartBrowser.

🔒 Security & Privacy

No packet inspection or credential access

Uses Chrome’s native profile isolation

VPN / No-VPN state lives in Chrome profiles only

Fully reversible

🧪 Limitations

Chrome profiles cannot share live sessions (by design)

VPN detection is profile-based (manual mapping)

First visit to a domain may take ~0.5s (subsequent visits cached)

🚀 Roadmap (Optional Enhancements)

System tray app with status icon

Auto-start on Windows login

Manual override hotkey (force VPN / No-VPN)

Per-domain pinning

Logging & diagnostics

📜 License

MIT License (or your preferred license)

👤 Author

Soroush Bazgir – Designed for secure and seamless network routing under restricted environments.

🟢 Next Steps After README

Once this README is in place:

git add README.md
git commit -m "Add polished project README"
git push


Then we can move confidently to:

STEP 8 — Set SmartBrowser as the Default Browser on Windows
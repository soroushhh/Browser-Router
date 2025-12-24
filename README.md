# SmartBrowser

**SmartBrowser** is a lightweight Windows tool that automatically opens websites in the correct **Chrome profile** (VPN or No-VPN) based on real network reachability. It’s ideal for environments with restricted access, where some sites require VPN and others work best without it.

---

## 🌟 Features

- **Automatic routing**
  - Blocked sites → VPN profile
  - Local sites → No-VPN profile
- **Network-aware**
  - Real TCP reachability tests
  - No static domain lists
- **Chrome profile support**
  - Keeps Google account, passwords, bookmarks, and extensions separate per profile
- **Fast & cached**
  - Routing decisions cached with TTL for instant performance
- **Search-friendly**
  - Single words → Google search
  - Domains → direct navigation
- **Windows integration**
  - Can be set as the default browser
- **Safe & reversible**
  - No Chrome hacks, no cookie sharing, no registry changes

---

## 🧠 How It Works

 User clicks a link
<br> &emsp;&emsp;&emsp;    ↓
<br> SmartBrowser.exe
<br> &emsp;&emsp;&emsp;    ↓
<br> Normalize input (URL or search)
<br> &emsp;&emsp;&emsp;    ↓
<br> Check cache
<br> &emsp;&emsp;&emsp;     ↓
<br> Network reachability test
<br> &emsp;&emsp;&emsp;    ↓
<br> Decide profile: VPN or No-VPN
<br> &emsp;&emsp;&emsp;    ↓
<br> Launch Chrome with correct profile text

---

## 📂 Project Structure
smart_browser/<br>
├── main.py<br>
├── config.py<br>
├── utils.py<br>
├── network.py<br>
├── decision.py<br>
├── launcher.py<br>
├── cache.py<br>
├── profiles.py<br>
├── route_cache.json<br>
├── README.md<br>

---

## ⚙️ Requirements

- Python 3.10+ (for development)  
- Windows 10+  
- Google Chrome with **two profiles**:
  - One with VPN extension enabled  
  - One without VPN extension

---

## 🔧 Configuration

Edit `config.py`:
```python
PROFILES = {
    "vpn": "Profile 2",
    "no_vpn": "Default"
}
```
⚠️ **Folder names must exactly match Chrome’s actual profile folders (e.g., Default, Profile 1, Profile 2).**
**You can run profiles.py to list your existing profiles programmatically.**

---

## ▶️ Usage (Development)
Bashpython main.py github.com
python main.py example.ir
python main.py google
Behavior examples:

InputOutcomegithub.comOpens in VPN profile (blocked)example.irOpens in No-VPN profile (local)googlePerforms Google search

## 🌍 Set as Default Browser (Windows)

1. Open Settings → Apps → Default apps
2. Scroll down and click Choose defaults by app
3. Select SmartBrowser
4. Assign it to HTTP, HTTPS, .htm, .html

Now all web links will automatically route through SmartBrowser.

## 🔒 Security & Privacy

No packet inspection or credential access
* Uses Chrome’s native profile isolation
* VPN / No-VPN state is defined only by your Chrome profiles
* Fully reversible – just reset default browser to Chrome


## 🧪 Limitations

* Chrome profiles cannot share live sessions (by design)
* VPN detection is profile-based (manual mapping in config)
* First visit to a new domain may take ~0.5s (subsequent visits are cached and instant)


## 🚀 Roadmap (Optional Enhancements)

* System tray app with status icon
* Auto-start on Windows login
* Manual override hotkey (force VPN / No-VPN)
* Per-domain pinning
* Logging & diagnostics


## 📜 License
__MIT License__

## 👤 Author
Soroush Bazgir – Built for seamless network routing under restricted environments.
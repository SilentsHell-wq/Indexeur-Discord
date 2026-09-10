# NANA

```text
███▄    █  ▄▄▄       ███▄    █  ▄▄▄
██ ▀█   █ ▒████▄     ██ ▀█   █ ▒████▄
▓██  ▀█ ██▒▒██  ▀█▄  ▓██  ▀█ ██▒▒██  ▀█▄
▓██▒  ▐▌██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒░██▄▄▄▄██
▒██░   ▓██░ ▓█   ▓██▒▒██░   ▓██░ ▓█   ▓██▒
░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒   ▓▒█░
░ ░░   ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ▒░  ▒   ▒▒ ░
   ░   ░ ░   ░   ▒      ░   ░ ░   ░   ▒
         ░       ░  ░         ░       ░  ░
```

> Discord message analysis & OSINT-oriented archiving tool.

**Developed by `silentShell`**

---

## Features

```text
[+] Discord API integration
[+] Server channel enumeration
[+] Channel selection
[+] User lookup
[+] Message collection
[+] Message filtering by author
[+] Attachment detection
[+] Reaction detection
[+] Mention detection
[+] Pinned message detection
[+] Email pattern detection
[+] Keyword frequency analysis
[+] Per-channel statistics
[+] JSON result export
[+] Terminal interface
[+] Animated startup
```

---

## Workflow

```text
             ┌──────────────┐
             │    NANA      │
             └──────┬───────┘
                    │
                    ▼
          ┌───────────────────┐
          │ Discord API Auth  │
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │   Server Target   │
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │ Channel Selection │
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │   User Selection  │
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │ Message Collection│
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │      Analysis     │
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │    JSON Export    │
          └───────────────────┘
```

---

## Installation

### Requirements

* Python 3.10+
* Discord account with access to the target server
* Appropriate permissions to access the requested channels

### Dependencies

```bash
pip install requests
```

---

## Usage

```bash
python nana.py
```

Startup:

```text
[+] NANA
[+] Extraction + Analyse Discord
[+] Developpe par silentShell

[1] Authenticate
[2] Configure credentials
[3] Quitter
```

After authentication:

```text
[?] ID du serveur: 123456789012345678

[+] 24 salons chat trouves

[?] Choisis les salons a scanner:
[all]   Scanner tous les salons
[3]     Scanner un salon
[1,2,3] Scanner plusieurs salons
[1-5]   Scanner une plage
```

---

## Analysis

NANA generates statistics such as:

```text
============================================================
                         ANALYSE
============================================================

STATISTIQUES:

  - Messages: 1842
  - Salons: 7
  - Fichiers joints: 13
  - Messages epingles: 4

SALONS:

  - #general: 724 messages ################
  - #chat: 481 messages ##########
  - #off-topic: 291 messages ######
```

Keyword analysis:

```text
MOTS CLES:

  - python: 91 ####################
  - server: 67 ##############
  - linux: 54 ###########
  - discord: 48 ##########
```

---

## Export

Results can be exported as JSON:

```text
nana_username_20260910_064500.json
```

Example structure:

```json
{
  "user": {},
  "server_id": "123456789",
  "channels_scanned": [],
  "analysis": {
    "total_messages": 1842,
    "channels": {},
    "emails": [],
    "top_words": {}
  },
  "messages": []
}
```

---

## Security

NANA is intended for:

```text
✓ Security research
✓ OSINT investigations with authorization
✓ Discord server administration
✓ Message archiving
✓ Personal data analysis
✓ Incident response
✓ CTF / lab environments
```

Do not use the tool to access Discord accounts, servers, channels, or private information without authorization.

**Never publish Discord authentication tokens, cookies, session data, or other credentials in a repository.**

For a public GitHub release, authentication should use a credential supplied explicitly by the operator rather than attempting to extract credentials from browsers or desktop applications.

---

## Roadmap

```text
[ ] Advanced message search
[ ] Date-range filtering
[ ] Regex search
[ ] Export to CSV
[ ] Export to HTML
[ ] SQLite database
[ ] Interactive statistics
[ ] Message timeline
[ ] Attachment index
[ ] Improved rate-limit handling
[ ] Modular plugin system
[ ] Configuration file
```

---

## Project Structure

```text
NANA/
│
├── nana.py
├── README.md
├── requirements.txt
│
├── data/
│   └── exports/
│
└── output/
```

---

## Disclaimer

NANA is provided for educational, research, administration, and authorized security-audit purposes.

The operator is responsible for ensuring that their use of the software complies with Discord's rules, applicable law, and the permissions governing the server and data being analyzed.

---

## Author

```text
╔══════════════════════════════════════╗
║              N A N A                 ║
║                                      ║
║          developed by                ║
║             silentShell              ║
╚══════════════════════════════════════╝
```

> `Extract. Analyze. Understand.`

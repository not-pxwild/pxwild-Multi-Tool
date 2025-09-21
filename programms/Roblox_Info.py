# Copyright (c) 2025 pxwild. All rights reserved.
# This software and its source code are proprietary and confidential.
# Unauthorized copying, modification, or distribution of this software,
# via any medium, is strictly prohibited without prior written permission.

import requests
import json
from datetime import datetime
from colorama import Fore, Style

red, green, yellow, white, reset = Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.WHITE, Style.RESET_ALL

def t():
    return datetime.now().strftime("%H:%M:%S")

BEFORE, AFTER = f"{red}[{reset}", f"{red}]{reset}"
INPUT, WAIT, ADD = f"{yellow}?{reset}", f"{yellow}*{reset}", f"{green}+{reset}"
BOX_WIDTH = 60

def format_line(label, value):
    line = f" {ADD} {label:<15}: {white}{value}{reset}"
    length_without_colors = len(remove_colors(f"{label:<15}: {value}"))
    padding = BOX_WIDTH - length_without_colors - 4
    return line + " " * max(0, padding) + f"{white}║{reset}"

def remove_colors(s):
    import re
    return re.sub(r"\x1b\[[0-9;]*m", "", s)

def get_roblox_info():
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        username = input(f"{BEFORE}{t()}{AFTER} {INPUT} Username -> {reset}").strip()
        if not username:
            print(f"{BEFORE}{t()}{AFTER} {red}Error: No username provided{reset}")
            return

        print(f"{BEFORE}{t()}{AFTER} {WAIT} Retrieving information...{reset}")

        r = requests.post(
            "https://users.roblox.com/v1/usernames/users",
            headers=headers,
            json={"usernames": [username], "excludeBannedUsers": True},
            timeout=10
        )
        if r.status_code != 200:
            print(f"{BEFORE}{t()}{AFTER} {red}Error: Failed to get user ID ({r.status_code}){reset}")
            return

        data = r.json()
        if not data.get("data"):
            print(f"{BEFORE}{t()}{AFTER} {red}Error: User not found{reset}")
            return

        user_id = data["data"][0]["id"]

        r = requests.get(f"https://users.roblox.com/v1/users/{user_id}", headers=headers, timeout=10)
        if r.status_code != 200:
            print(f"{BEFORE}{t()}{AFTER} {red}Error: Failed to get user details ({r.status_code}){reset}")
            return
        api = r.json()

        friends = requests.get(f"https://friends.roblox.com/v1/users/{user_id}/friends/count", headers=headers).json().get("count", "N/A")
        followers = requests.get(f"https://friends.roblox.com/v1/users/{user_id}/followers/count", headers=headers).json().get("count", "N/A")
        following = requests.get(f"https://friends.roblox.com/v1/users/{user_id}/followings/count", headers=headers).json().get("count", "N/A")
        premium = requests.get(f"https://premiumfeatures.roblox.com/v1/users/{user_id}/validate-membership", headers=headers).status_code == 200

        userid = api.get("id", "N/A")
        display = api.get("displayName", "N/A")
        uname = api.get("name", "N/A")
        desc = api.get("description", "No description")
        created = api.get("created", "N/A")
        banned = api.get("isBanned", "N/A")
        appname = api.get("externalAppDisplayName", "N/A")
        verified = api.get("hasVerifiedBadge", "N/A")

        if created != "N/A":
            try:
                created = datetime.strptime(created, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S")
            except:
                pass

        lines = [
            format_line("Username", uname),
            format_line("User ID", userid),
            format_line("Display Name", display),
            format_line("Description", desc[:40] + ("..." if len(desc) > 40 else "")),
            format_line("Created", created),
            format_line("Banned", banned),
            format_line("External App", appname),
            format_line("Verified Badge", verified),
            format_line("Premium", premium),
            format_line("Friends", friends),
            format_line("Followers", followers),
            format_line("Following", following),
        ]

        print(f"\n{white}╔{'═' * (BOX_WIDTH-2)}╗{reset}")
        for line in lines:
            print(f"{white}║{reset}" + line[1:])
        print(f"{white}╚{'═' * (BOX_WIDTH-2)}╝{reset}\n")

        input(f"{BEFORE}{t()}{AFTER} {INPUT} Press Enter to continue...{reset}")

    except requests.exceptions.RequestException as e:
        print(f"{BEFORE}{t()}{AFTER} {red}Network error: {e}{reset}")
    except (json.JSONDecodeError, KeyError) as e:
        print(f"{BEFORE}{t()}{AFTER} {red}Data error: {e}{reset}")
    except Exception as e:
        print(f"{BEFORE}{t()}{AFTER} {red}Error: {e}{reset}")

def main():
    get_roblox_info()

if __name__ == "__main__":

    main()

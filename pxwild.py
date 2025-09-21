import os
import time
import importlib.util
from colorama import init, Fore
from pystyle import Colors, Colorate

init(autoreset=True)
red, green, yellow, blue, reset = Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.RESET

TOOL_NAME = "PXWILD"
OSINT_NAME = "OSINT-PXWILD"
VERSION = "v1.0"
DEVELOPER = "by pxwild"
PROGRAMS_DIR = "programms"
OSINT_DIR = "osint_tools"

option_definitions = {
    "01": "Phishing-Builder",
    "02": "Virus-Builder",
    "03": "Roblox_Info", 
    "04": "ransomware_builder", 
    "05": "DDoS",
    "06": "Keylogger_builder", 
    "07": "RAT_builder",
}

osint_definitions = {
    "01": "DNS-History-Check", "02": "Reverse-IP-Lookup", "03": "Google-Dorking",
    "04": "Social-Media-Lookup", "05": "Get-Phone-Info", "06": "Website-Screenshot",
    "07": "Email-Breach-Checker", "08": "SSL-Certificate-Info", "09": "Website-Tech-Stack",
    "10": "Admin-Panel-Scan", "11": "Website-Crawler", "12": "Hash-Identifier",
    "13": "Pastebin-Dump-Search", "14": "Username-Checker", "15": "Website-Screenshot",
    "16": "File-Metadata-Extractor", "17": "MAC-Address-Lookup", "18": "DNS-Lookup",
    "19": "Username-Availability", "20": "WHOIS-Lookup", "21": "Dark-Web-Search",
    "22": "IP-Blacklist-Check", "23": "Subdomain-Finder", "24": "Extract-Links",
    "25": "Email-Header-Analyzer", "26": "Get-IP-Info", "27": "Website-Screenshot-Alt",
    "28": "Check-Breaches", "29": "IP-Geolocation", "30": "Exit-Tool"
}

def discover_programs():
    if not os.path.exists(PROGRAMS_DIR):
        os.makedirs(PROGRAMS_DIR)
    return {
        key: {"display_name": value, "script_name": value.replace(" ", "_").replace("-", "_")}
        for key, value in option_definitions.items()
    }

def discover_osint_tools():
    if not os.path.exists(OSINT_DIR):
        os.makedirs(OSINT_DIR)
    return {
        key: {"display_name": value.replace("-", " "), "script_name": value.replace(" ", "_").replace("-", "_")}
        for key, value in osint_definitions.items()
    }

options = discover_programs()
osint_tools = discover_osint_tools()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print(Colorate.Horizontal(Colors.red_to_black, f""" 
                                d8b 888      888 
                                Y8P 888      888 
                                    888      888 
88888b.  888  888 888  888  888 888 888  .d88888 
888 "88b `Y8bd8P' 888  888  888 888 888 d88" 888 
888  888   X88K   888  888  888 888 888 888  888 
888 d88P .d8""8b. Y88b 888 d88P 888 888 Y88b 888 
88888P"  888  888  "Y8888888P"  888 888  "Y88888 
888                                              
888             {TOOL_NAME} {VERSION} | {DEVELOPER}
"""))

def print_osint_banner():
    print(Colorate.Horizontal(Colors.blue_to_black, f"""
     ▄▀▀▀▀▄   ▄▀▀▀▀▄  ▄▀▀█▀▄    ▄▀▀▄ ▀▄  ▄▀▀▀█▀▀▄ 
    █      █ █ █   ▐ █   █  █  █  █ █ █ █    █  ▐ 
    █      █    ▀▄   ▐   █  ▐  ▐  █  ▀█ ▐   █     
    ▀▄    ▄▀ ▀▄   █      █       █   █     █      
      ▀▀▀▀    █▀▀▀    ▄▀▀▀▀▀▄  ▄▀   █    ▄▀       
              ▐      █       █ █    ▐   █         
                     ▐       ▐ ▐        ▐         
       {OSINT_NAME} {VERSION} | {DEVELOPER}
"""))

def print_menu():
    print(Colorate.Horizontal(Colors.red_to_black, """
╔═══════════════════════════════════════════════╗
║                 MENU OPTIONS                  ║
╠═══════════════════════════════════════════════╣
║ 1. Phishing Builder                           ║
║ 2. Virus Builder                              ║
║ 3. Roblox Info                                ║
║ 4. ransomware builder                         ║
║ 5. DDoS                                       ║
║ 6. Keylogger Builder                          ║
║ 7. RAT builder                                ║
║                                               ║
║ N. Next (OSINT Tools)                         ║
║ Q. Exit                                       ║
╚═══════════════════════════════════════════════╝
"""))

def print_osint_menu():
    print(Colorate.Horizontal(Colors.blue_to_black, """
╔═════════════════════════════════════════════════════════╗
║                       OSINT TOOLS                       ║
╠═════════════════════════════════════════════════════════╣
║ 01. DNS History Check       16. File Metadata Extractor ║
║ 02. Reverse IP Lookup       17. MAC Address Lookup      ║
║ 03. Google Dorking          18. DNS Lookup              ║
║ 04. Social Media Lookup     19. Username Availability   ║
║ 05. Get Phone Number Info   20. WHOIS Lookup            ║
║ 06. Website Screenshot      21. Dark Web Search         ║
║ 07. Email Breach Checker    22. IP Blacklist Check      ║
║ 08. SSL Certificate Info    23. Subdomain Finder        ║
║ 09. Website Tech Stack      24. Extract Links           ║
║ 10. Admin Panel Scan        25. Email Header Analyzer   ║
║ 11. Website Crawler         26. Get IP Info             ║
║ 12. Hash Identifier         27. Website Screenshot Alt  ║
║ 13. Pastebin Dump Search    28. Check Breaches          ║
║ 14. Username Checker        29. IP Geolocation          ║
║ 15. Website Screenshot      30. Exit Tool               ║
║ B. Back to Main Menu                                    ║
║ Q. Exit                                                 ║
╚═════════════════════════════════════════════════════════╝
"""))

def normalize_choice(choice):
    return f"0{choice}" if choice.isdigit() and len(choice) == 1 else choice

def run_program(program_name, directory=PROGRAMS_DIR):
    program_path = os.path.join(directory, f"{program_name}.py")
    if not os.path.exists(program_path):
        print(f"{red}[!] {program_name} not found in {directory}/{reset}")
        return False
    try:
        spec = importlib.util.spec_from_file_location(program_name, program_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if hasattr(module, 'main'):
            module.main()
        else:
            print(f"{yellow}[!] {program_name} has no main(){reset}")
        return True
    except Exception as e:
        print(f"{red}[!] Error running {program_name}: {e}{reset}")
        return False

def osint_section():
    while True:
        clear_screen()
        print_osint_banner()
        print_osint_menu()
        choice = input(f"{blue}Select OSINT tool (01-30), B to back, Q to quit: {reset}")
        if choice.upper() == 'B':
            return
        if choice.upper() == 'Q':
            print(f"\n{blue}[!] Exiting {OSINT_NAME}. Stay stealthy.{reset}")
            exit(0)
        normalized_choice = normalize_choice(choice)
        if normalized_choice in osint_tools:
            tool = osint_tools[normalized_choice]
            print(f"\n{blue}[+] Starting {tool['display_name']}...{reset}")
            time.sleep(1)
            success = run_program(tool['script_name'], OSINT_DIR)
            if success:
                print(f"\n{blue}[+] {tool['display_name']} finished.{reset}")
            else:
                print(f"\n{red}[!] {tool['display_name']} failed.{reset}")
            input(f"\n{blue}Press Enter to return...{reset}")
        else:
            print(f"\n{red}[!] Invalid option.{reset}")
            time.sleep(1)

def main():
    while True:
        clear_screen()
        print_banner()
        print_menu()
        choice = input(f"{red}Select option (1-6), N for OSINT, Q to quit: {reset}") 
        if choice.upper() == 'N':
            osint_section()
            continue
        if choice.upper() == 'Q':
            print(f"\n{red}[!] Exiting {TOOL_NAME}. Stay stealthy.{reset}")
            break
        normalized_choice = normalize_choice(choice)
        if normalized_choice in options:
            program = options[normalized_choice]
            print(f"\n{green}[+] Starting {program['display_name'].replace('-', ' ')}...{reset}")
            time.sleep(1)
            success = run_program(program['script_name'])
            if success:
                print(f"\n{green}[+] {program['display_name'].replace('-', ' ')} finished.{reset}")
            else:
                print(f"\n{red}[!] {program['display_name'].replace('-', ' ')} failed.{reset}")
            input(f"\n{red}Press Enter to return...{reset}")
        else:
            print(f"\n{red}[!] Invalid option.{reset}")
            time.sleep(1)

if __name__ == "__main__":
    main()
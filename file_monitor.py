import hashlib
import os
import time
import json
import smtplib
import getpass  # ✅ To get current user
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ✅ Updated file paths
FILES_TO_MONITOR = [
    "C:/Users/ASUS/OneDrive/Desktop/test1.txt",
    "C:/Users/ASUS/OneDrive/Desktop/test2.txt"
]

HASHES_FILE = "file_hashes.json"
REPORT_FILE = "forensics_report.json"
MONITOR_INTERVAL = 120  # 2 min

# ✅ Updated email config
EMAIL_CONFIG = {
    "from_email": "roseroshini2805@gmail.com",
    "password": "xfak bfnf doem rbif",  # App password
    "to_email": "roseroshini2805@gmail.com",
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587
}

def calculate_file_hash(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return None

def load_hashes():
    if os.path.exists(HASHES_FILE):
        with open(HASHES_FILE, "r") as f:
            return json.load(f)
    return {}

def save_hashes(hashes):
    with open(HASHES_FILE, "w") as f:
        json.dump(hashes, f, indent=4)

def generate_forensics_report(file_path, old_hash, new_hash):
    user = getpass.getuser()  # ✅ Get current logged-in user
    report = {
        "file": file_path,
        "initial_hash": old_hash,
        "current_hash": new_hash,
        "timestamp": time.ctime(),
        "user": user
    }
    with open(REPORT_FILE, "a") as f:
        f.write(json.dumps(report, indent=4) + ",\n")
    print(f"📝 Forensic report updated for {file_path} by user: {user}")

def send_email_alert(subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_CONFIG["from_email"]
        msg['To'] = EMAIL_CONFIG["to_email"]
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(EMAIL_CONFIG["smtp_server"], EMAIL_CONFIG["smtp_port"])
        server.starttls()
        server.login(EMAIL_CONFIG["from_email"], EMAIL_CONFIG["password"])
        server.sendmail(EMAIL_CONFIG["from_email"], EMAIL_CONFIG["to_email"], msg.as_string())
        server.quit()
        print("✅ Email alert sent.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

def monitor_files():
    print("🔍 Starting file integrity monitoring...")
    stored_hashes = load_hashes()

    while True:
        for file_path in FILES_TO_MONITOR:
            new_hash = calculate_file_hash(file_path)
            if not new_hash:
                continue

            old_hash = stored_hashes.get(file_path)
            if old_hash is None:
                stored_hashes[file_path] = new_hash
                save_hashes(stored_hashes)
                continue

            if new_hash != old_hash:
                print(f"🚨 ALERT: Change detected in {file_path}")
                generate_forensics_report(file_path, old_hash, new_hash)

                user = getpass.getuser()
                subject = f"File Change Detected: {file_path}"
                body = (
                    f"File: {file_path}\n"
                    f"Time: {time.ctime()}\n"
                    f"Old Hash: {old_hash}\n"
                    f"New Hash: {new_hash}\n"
                    f"User: {user}"
                )
                send_email_alert(subject, body)

                stored_hashes[file_path] = new_hash
                save_hashes(stored_hashes)

        print(f"🕒 Sleeping for {MONITOR_INTERVAL} seconds...\n")
        time.sleep(MONITOR_INTERVAL)

if __name__ == "__main__":
    monitor_files()

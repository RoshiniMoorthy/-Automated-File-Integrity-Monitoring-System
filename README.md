# 🔐 Automated File Integrity Monitoring System

A real-time Python-based file integrity monitoring system for cyber forensics. This tool continuously monitors specified files and directories for unauthorized modifications, deletions, or additions and provides forensic reports for digital investigation.

---

## 🚀 Features

- 📁 Monitors files and directories in real-time
- 🔍 Detects modifications, deletions, and new file additions
- 🧾 Generates forensic reports in JSON format
- 📬 Optional integration with email alerts
- 📊 Visualize file activity history (future enhancement)
- 🔐 Ideal for digital forensics and cybersecurity use cases

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Hashlib** – for cryptographic hashing
- **JSON** – for report generation and configuration
- (Optional) **smtplib/email** – for email notifications

---

## 📂 Project Structure

📁 Automated-File-Integrity-Monitoring-System/
├── file_monitor.py # Main monitoring script
├── file_hashes.json # Stores original file hashes
├── forensics_report.json # Records detected changes
├── test1.txt / test2.txt # Sample files to monitor
└── README.md # Project documentation


---

## ⚙️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/RoshiniMoorthy/Automated-File-Integrity-Monitoring-System.git
   cd Automated-File-Integrity-Monitoring-System
2. Run the monitor:
    python file_monitor.py

📌 Use Case Scenarios
Cyber Forensics Investigations

Monitoring Critical System Files

Real-time Intrusion Detection

Secure File Change Tracking

🧑‍💻 Author
Roshini Moorthy

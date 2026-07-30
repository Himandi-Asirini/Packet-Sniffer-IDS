# 🛡️ Packet Sniffer IDS

A Python-based **Packet Sniffer and Intrusion Detection System (IDS)** developed as part of my cybersecurity learning journey. This project captures live network traffic, analyzes packets, detects suspicious activity, and generates multiple security reports.

---

## ✨ Features

### 📡 Packet Monitoring
- Capture live network packets using Scapy
- Display source and destination IP addresses
- Detect network protocols (TCP, UDP, ICMP)
- Interactive protocol selection (All / TCP / UDP / ICMP)
- Command-line protocol selection
- User-defined packet capture count
- Continuous monitoring mode
- Timestamp every captured packet

### 📊 Traffic Analysis
- Generate packet statistics
- Count connections per IP address
- Identify the most active IP (Top Talker)
- Count TCP connections for each IP
- Track unique destination ports

### 🚨 Security Monitoring
- Detect possible port scans using unique destination ports
- Detect suspicious network activity based on packet thresholds
- Reduce false positives during normal network browsing
- Generate real-time security alerts

### 📝 Logging & Reporting
- Export packet logs to `packet_logs.txt`
- Generate security reports in `security_report.txt`
- Export packet statistics to `packet_statistics.csv`
- Export IP address packet counts
- Export destination port information

---

## 🛠️ Technologies Used

- Python 3
- Scapy
- argparse
- CSV Module
- Networking Concepts
- Intrusion Detection Concepts

---

## 📂 Project Structure

```text
Packet-Sniffer/
│
├── images/
│   ├── live_capture.png
│   ├── statistics.png
│   ├── port_scan_detection.png
│   ├── security_report.png
│   ├── v13_menu.png
│   ├── v13_packet_count.png
│   ├── v14_csv_terminal.png
│   ├── v14_csv_excel.png
│   ├── v15_interactive_menu.png
│   ├── v15_command_line_mode.png
│   ├── v16_continuous_monitoring.png
│   └── v16_stop_capture.png
│
├── packet_sniffer.py
├── packet_logs.txt
├── security_report.txt
├── packet_statistics.csv
├── README.md
└── .gitignore
```

---

## ▶️ How to Run

### Clone the repository

```bash
git clone https://github.com/Himandi-Asirini/Packet-Sniffer-IDS.git
```

### Navigate into the project

```bash
cd Packet-Sniffer-IDS
```

### Install dependencies

```bash
pip install scapy
```

---

## 🖥️ Run in Interactive Mode

```bash
python packet_sniffer.py
```

The program will let you:

- Select protocol (All / TCP / UDP / ICMP)
- Choose Fixed Packet Capture or Continuous Monitoring
- Enter the number of packets (Fixed mode)

---

## 💻 Run in Command-Line Mode

Capture TCP packets

```bash
python packet_sniffer.py --protocol tcp --count 20
```

Capture UDP packets

```bash
python packet_sniffer.py --protocol udp --count 20
```

Capture ICMP packets

```bash
python packet_sniffer.py --protocol icmp --count 20
```

Capture all packets

```bash
python packet_sniffer.py --protocol all --count 20
```

---

## 📈 Current Version

**Version 16**

### ✅ Implemented Features

- Live Packet Capture
- Interactive Protocol Selection
- Command-Line Argument Support
- Fixed Packet Capture
- Continuous Monitoring Mode
- User-defined Packet Capture Count
- Menu Input Validation
- Packet Count Validation
- Timestamp Logging
- TCP / UDP / ICMP Detection
- Packet Statistics
- Connection Counts
- Top Talker Detection
- TCP Connection Counting
- Unique Destination Port Tracking
- Improved Port Scan Detection
- Suspicious Activity Detection
- Packet Log Export
- Security Report Generation
- CSV Report Export

---

## 📜 Version History

### Version 10
- Live packet capture
- Packet statistics
- Connection counting
- Top Talker detection
- Packet logging
- Security report generation

### Version 11
- TCP connection counting
- Basic TCP threshold-based port scan detection

### Version 12
- Improved port scan detection using unique destination ports
- Reduced false positives during normal HTTPS traffic

### Version 13
- Interactive packet capture menu
- Protocol filtering (All, TCP, UDP, ICMP)
- User-selectable packet capture count
- Menu input validation
- Packet count validation

### Version 14
- CSV report export
- Export packet statistics
- Export IP address packet counts
- Export destination port information

### Version 15
- Added command-line argument support using argparse
- Capture packets without interactive prompts
- Support protocol selection using `--protocol`
- Support packet count using `--count`
- Retained interactive mode as the default

### Version 16
- Added Continuous Monitoring Mode
- Capture packets until the user presses **Ctrl + C**
- Automatic report generation after monitoring stops
- Improved monitoring workflow with graceful shutdown messages

---

## 🚀 Future Improvements

- DNS hostname resolution
- Packet size analysis
- JSON report export
- Dashboard for live traffic visualization
- Packet filtering by IP address
- SYN scan detection
- Email alert notifications
- GeoIP lookup for external IP addresses
- Console color support

---

## 📸 Screenshots

### Live Packet Capture

![Live Packet Capture](images/live_capture.png)

---

### Traffic Statistics

![Traffic Statistics](images/statistics.png)

---

### Port Scan Detection

![Port Scan Detection](images/port_scan_detection.png)

---

### Security Report

![Security Report](images/security_report.png)

---

### Interactive Menu

![Interactive Menu](images/v15_interactive_menu.png)

---

### Command-Line Mode

![Command-Line Mode](images/v15_command_line_mode.png)

---

### CSV Report Export

![CSV Report Export](images/v14_csv_terminal.png)

---

### CSV Report Preview

![CSV Report Preview](images/v14_csv_excel.png)

---

### Continuous Monitoring

![Continuous Monitoring](images/v16_continuous_monitoring.png)

---

### Monitoring Stopped

![Monitoring Stopped](images/v16_stop_capture.png)

---

## 👩‍💻 Author

**Himandi Asirini**

Cyber Security Undergraduate | Python Developer | Network Security Enthusiast
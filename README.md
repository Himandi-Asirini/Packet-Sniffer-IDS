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
│   └── v15_command_line_mode.png
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

### Run in Interactive Mode

```bash
python packet_sniffer.py
```

### Run in Command-Line Mode

Capture TCP packets:

```bash
python packet_sniffer.py --protocol tcp --count 20
```

Capture UDP packets:

```bash
python packet_sniffer.py --protocol udp --count 20
```

Capture ICMP packets:

```bash
python packet_sniffer.py --protocol icmp --count 20
```

Capture all packets:

```bash
python packet_sniffer.py --protocol all --count 20
```

---

## 📈 Current Version

**Version 15**

### ✅ Implemented Features

- Live Packet Capture
- Interactive Protocol Selection
- Command-Line Argument Support
- User-defined Packet Capture Count
- Menu Input Validation
- Packet Count Validation Loop
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
- Unique destination port tracking
- Improved port scan detection using unique destination ports
- Reduced false positives during normal HTTPS traffic

### Version 13
- Interactive packet capture menu
- Protocol filtering (All, TCP, UDP, ICMP)
- User-selectable packet capture count
- Menu input validation
- Packet count validation with retry loop

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

---

## 🚀 Future Improvements

- Continuous monitoring mode
- JSON report export
- Dashboard for live traffic visualization
- Packet filtering by IP address
- SYN scan detection
- Email alert notifications
- GeoIP lookup for external IP addresses
- Packet size analysis
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

## 👩‍💻 Author

**Himandi Asirini**

Cyber Security Undergraduate | Python Developer | Network Security Enthusiast
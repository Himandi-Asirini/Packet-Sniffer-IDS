# 🛡️ Packet Sniffer IDS

A Python-based **Packet Sniffer and Intrusion Detection System (IDS)** developed as part of my cybersecurity learning journey. This project captures live network traffic, analyzes packets, detects suspicious activity, and generates security reports.

---

## ✨ Features

### 📡 Packet Monitoring
- Capture live network packets using Scapy
- Display source and destination IP addresses
- Detect network protocols (TCP, UDP, ICMP)
- Timestamp every captured packet

### 📊 Traffic Analysis
- Generate packet statistics
- Count connections per IP address
- Identify the most active IP (Top Talker)
- Count TCP connections for each IP

### 🚨 Security Monitoring
- Detect possible port scanning based on TCP connection thresholds
- Detect suspicious network activity based on packet thresholds
- Generate real-time security alerts

### 📝 Logging & Reporting
- Export captured packet logs to `packet_logs.txt`
- Generate security reports in `security_report.txt`
- Save timestamps for every captured packet

---

## 🛠️ Technologies Used

- Python 3
- Scapy
- Networking Concepts
- Intrusion Detection Concepts

---

## 📂 Project Structure

```
Packet-Sniffer/
│
├── packet_sniffer.py
├── packet_logs.txt
├── security_report.txt
├── README.md
├── .gitignore
```

---

## ▶️ How to Run

### Clone the repository

```bash
git clone https://github.com/Himandi-Asirini/Packet-Sniffer-IDS.git
```

### Navigate to the project

```bash
cd Packet-Sniffer-IDS
```

### Install Scapy

```bash
pip install scapy
```

### Run the program

```bash
python packet_sniffer.py
```

---

## 📈 Current Version

**Version 11**

### Implemented Features

- ✅ Live Packet Capture
- ✅ Timestamp Logging
- ✅ TCP / UDP / ICMP Detection
- ✅ Packet Statistics
- ✅ Connection Counts
- ✅ Top Talker Detection
- ✅ TCP Connection Counting
- ✅ Basic Port Scan Detection
- ✅ Suspicious Activity Detection
- ✅ Packet Log Export
- ✅ Security Report Generation

---

## 🚀 Future Improvements

- Detect scans using multiple destination ports
- Dashboard for live traffic visualization
- CSV report generation
- Interactive command-line menu
- Packet filtering by protocol
- Export reports in JSON format
- Email alert notifications
- GeoIP lookup for external IP addresses

---

## 👩‍💻 Author

**Himandi Asirini**

Cyber Security Undergraduate | Python Developer | Network Security Enthusiast

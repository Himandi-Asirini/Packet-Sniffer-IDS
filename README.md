# Packet Sniffer IDS

A Python-based Packet Sniffer and Intrusion Detection System (IDS) developed as part of my cybersecurity learning journey.

## Project Overview

This project captures live network traffic and performs basic intrusion detection by analyzing packet activity, identifying the most active hosts, detecting suspicious behavior based on configurable thresholds, and generating security reports.

The project was built to strengthen practical skills in network monitoring, packet analysis, intrusion detection, and cybersecurity defense concepts.

---

## Features

### Packet Monitoring
- Capture live network packets using Scapy
- Display source and destination IP addresses
- Detect network protocols (TCP, UDP, ICMP)
- Timestamp captured packets

### Traffic Analysis
- Generate packet statistics
- Count connections per IP address
- Identify the most active IP address (Top Talker)

### Security Monitoring
- Detect suspicious activity based on configurable thresholds
- Generate security alerts
- Monitor network communication patterns

### Logging & Reporting
- Export packet logs to TXT files
- Generate security reports
- Record packet activity with timestamps

---

## Technologies Used

- Python
- Scapy
- Networking Concepts
- Intrusion Detection Concepts
- Git & GitHub

---

## Current Status

### Version 10 Completed

Implemented Features:

- Packet Capture
- Source & Destination IP Detection
- Protocol Detection
- Packet Statistics
- Packet Log Export
- Connection Counting
- Top Talker Detection
- Suspicious Activity Detection
- Security Report Generation
- Timestamped Packet Logging

---

## Example Output

```text
2026-06-10 14:46:02 | 192.168.1.4 --> 146.75.46.172 | TCP

===== Statistics =====
TCP Packets : 20
UDP Packets : 0
ICMP Packets: 0

===== Top Talker =====
Most Active IP: 192.168.1.4
Packet Count : 10

===== Suspicious Activity Detection =====
No suspicious activity detected.
```

---

## Future Improvements

- Port Scan Detection
- Interactive Menu System
- CSV Report Export
- Dashboard Visualization
- Real-Time Monitoring Dashboard
- Enhanced Alerting Mechanisms

---

## Learning Outcomes

Through this project, I gained practical experience in:

- Network Traffic Analysis
- Packet Inspection
- Intrusion Detection Fundamentals
- Python Programming
- Security Monitoring Concepts
- Git and GitHub Workflow

---

## Repository

GitHub Repository:

https://github.com/Himandi-Asirini/Packet-Sniffer-IDS

---

## Author

**Himandi Asirini**

Cybersecurity Undergraduate | SLIIT
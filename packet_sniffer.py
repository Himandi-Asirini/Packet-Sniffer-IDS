from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from datetime import datetime

# ==========================
# Configuration
# ==========================

ALERT_THRESHOLD = 10
PORT_SCAN_THRESHOLD = 8

# ==========================
# Statistics
# ==========================

tcp_count = 0
udp_count = 0
icmp_count = 0

# ==========================
# Storage
# ==========================

packet_logs = []
connection_counts = {}
port_scan_counts = {}
port_scan_ports = {}

# ==========================
# Packet Processing
# ==========================


def process_packet(packet):

    global tcp_count, udp_count, icmp_count

    if packet.haslayer(IP):

        source_ip = packet[IP].src
        destination_ip = packet[IP].dst

        if packet.haslayer(TCP):
            protocol = "TCP"
            tcp_count += 1

            destination_port = packet[TCP].dport

            if source_ip in port_scan_counts:
                port_scan_counts[source_ip] += 1
            else:
                port_scan_counts[source_ip] = 1

            if source_ip not in port_scan_ports:
                port_scan_ports[source_ip] = set()

            port_scan_ports[source_ip].add(destination_port)

        elif packet.haslayer(UDP):
            protocol = "UDP"
            udp_count += 1

        elif packet.haslayer(ICMP):
            protocol = "ICMP"
            icmp_count += 1

        else:
            protocol = "Other"

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_entry = (
            f"{timestamp} | "
            f"{source_ip} --> {destination_ip} | "
            f"{protocol}"
        )

        print(log_entry)

        packet_logs.append(log_entry)

        if source_ip in connection_counts:
            connection_counts[source_ip] += 1
        else:
            connection_counts[source_ip] = 1


# ==========================
# Start Capture
# ==========================

print("========== Packet Sniffer IDS ==========")
print("1. Capture All Packets")
print("2. Capture TCP Packets")
print("3. Capture UDP Packets")
print("4. Capture ICMP Packets")

choice = input("\nChoose an option (1-4): ")

capture_filter = None

if choice == "1":
    capture_filter = None

elif choice == "2":
    capture_filter = "tcp"

elif choice == "3":
    capture_filter = "udp"

elif choice == "4":
    capture_filter = "icmp"

else:
    print("\nInvalid option selected.")
    print("Please run the program again and choose a number between 1 and 4.")
    exit()

while True:

    packet_count = input("\nEnter the number of packets to capture: ")

    if packet_count.isdigit() and int(packet_count) > 0:
        packet_count = int(packet_count)
        break

    print("\nInvalid packet count.")
    print("Please enter a positive number.")

print(f"\nCapturing {packet_count} packets...\n")

sniff(
    count=packet_count,
    prn=process_packet,
    filter=capture_filter
)

print("\nCapture Complete!")

# ==========================
# Statistics
# ==========================

print("\n===== Statistics =====")
print(f"TCP Packets : {tcp_count}")
print(f"UDP Packets : {udp_count}")
print(f"ICMP Packets: {icmp_count}")

# ==========================
# Save Packet Logs
# ==========================

with open("packet_logs.txt", "w") as file:

    for log in packet_logs:
        file.write(log + "\n")

print("\nPacket logs saved to packet_logs.txt")

# ==========================
# Connection Counts
# ==========================

print("\n===== Connection Counts =====")

for ip, count in connection_counts.items():
    print(f"{ip} : {count} packets")

# ==========================
# Top Talker
# ==========================

top_ip = None

if connection_counts:

    top_ip = max(connection_counts, key=connection_counts.get)

    print("\n===== Top Talker =====")
    print(f"Most Active IP: {top_ip}")
    print(f"Packet Count : {connection_counts[top_ip]}")

# ==========================
# TCP Connection Counts
# ==========================

print("\n===== TCP Connection Counts =====")

for ip, count in port_scan_counts.items():
    print(f"{ip} : {count} TCP packets")

print("\n===== Destination Ports =====")

for ip, ports in port_scan_ports.items():
    print(f"{ip} -> {sorted(ports)}")

# ==========================
# Port Scan Detection
# ==========================

print("\n===== Port Scan Detection =====")

port_scan_found = False

for ip, ports in port_scan_ports.items():

    if len(ports) >= 5:

        port_scan_found = True

        print("[WARNING] Possible Port Scan Detected")
        print(f"Source IP : {ip}")
        print(f"Unique Destination Ports : {len(ports)}")
        print(f"Ports : {sorted(ports)}\n")

if not port_scan_found:
    print("No port scan detected.")

# ==========================
# Suspicious Activity Detection
# ==========================

print("\n===== Suspicious Activity Detection =====")

suspicious_found = False

for ip, count in connection_counts.items():

    if count > ALERT_THRESHOLD:

        suspicious_found = True

        print(f"[ALERT] Suspicious IP Detected: {ip}")
        print(f"Packet Count: {count}\n")

if not suspicious_found:
    print("No suspicious activity detected.")

# ==========================
# Security Report
# ==========================

with open("security_report.txt", "w") as report:

    report.write("========== SECURITY REPORT ==========\n\n")

    report.write("Packet Statistics\n")
    report.write("------------------------------\n")
    report.write(f"TCP Packets : {tcp_count}\n")
    report.write(f"UDP Packets : {udp_count}\n")
    report.write(f"ICMP Packets: {icmp_count}\n\n")

    report.write("Connection Counts\n")
    report.write("------------------------------\n")

    for ip, count in connection_counts.items():
        report.write(f"{ip} : {count} packets\n")

    report.write("\n")

    if top_ip:

        report.write("Top Talker\n")
        report.write("------------------------------\n")
        report.write(f"Most Active IP : {top_ip}\n")
        report.write(
            f"Packet Count   : {connection_counts[top_ip]}\n\n"
        )

    report.write("TCP Connection Counts\n")
    report.write("------------------------------\n")

    for ip, count in port_scan_counts.items():
        report.write(f"{ip} : {count} TCP packets\n")

    report.write("\n")

    report.write("Port Scan Detection\n")
    report.write("------------------------------\n")

    port_scan_found = False

    for ip, ports in port_scan_ports.items():

        if len(ports) >= 5:

            port_scan_found = True

            report.write("Possible Port Scan Detected\n")
            report.write(f"Source IP : {ip}\n")
            report.write(f"Unique Destination Ports : {len(ports)}\n")
            report.write(f"Ports : {sorted(ports)}\n\n")

    if not port_scan_found:
        report.write("No port scan detected.\n")

    report.write("\n")

    report.write("Suspicious Activity Detection\n")
    report.write("------------------------------\n")

    suspicious_found = False

    for ip, count in connection_counts.items():

        if count > ALERT_THRESHOLD:

            suspicious_found = True

            report.write(f"Suspicious IP : {ip}\n")
            report.write(f"Packet Count : {count}\n\n")

    if not suspicious_found:
        report.write("No suspicious activity detected.\n")

print("\nSecurity report saved to security_report.txt")
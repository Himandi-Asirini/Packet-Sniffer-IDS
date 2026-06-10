from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from datetime import datetime

# Configuration
ALERT_THRESHOLD = 10

# Statistics
tcp_count = 0
udp_count = 0
icmp_count = 0

# Storage
packet_logs = []
connection_counts = {}


def process_packet(packet):

    global tcp_count, udp_count, icmp_count

    if packet.haslayer(IP):

        source_ip = packet[IP].src
        destination_ip = packet[IP].dst

        if packet.haslayer(TCP):
            protocol = "TCP"
            tcp_count += 1

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


print("Capturing 20 packets...\n")

sniff(count=20, prn=process_packet)

print("\nCapture Complete!")

# Statistics
print("\n===== Statistics =====")
print(f"TCP Packets : {tcp_count}")
print(f"UDP Packets : {udp_count}")
print(f"ICMP Packets: {icmp_count}")

# Save Packet Logs
with open("packet_logs.txt", "w") as file:

    for log in packet_logs:
        file.write(log + "\n")

print("\nPacket logs saved to packet_logs.txt")

# Connection Counts
print("\n===== Connection Counts =====")

for ip, count in connection_counts.items():
    print(f"{ip} : {count} packets")

# Top Talker
if connection_counts:

    top_ip = max(
        connection_counts,
        key=connection_counts.get
    )

    print("\n===== Top Talker =====")
    print(f"Most Active IP: {top_ip}")
    print(
        f"Packet Count : "
        f"{connection_counts[top_ip]}"
    )

# Suspicious Activity Detection
print("\n===== Suspicious Activity Detection =====")

suspicious_found = False

for ip, count in connection_counts.items():

    if count > ALERT_THRESHOLD:

        suspicious_found = True

        print(
            f"[ALERT] Suspicious IP Detected: {ip}"
        )

        print(f"Packet Count: {count}\n")

if not suspicious_found:
    print("No suspicious activity detected.")

# Security Report
with open("security_report.txt", "w") as report:

    report.write(
        "=== SECURITY REPORT ===\n\n"
    )

    report.write(
        f"TCP Packets: {tcp_count}\n"
    )

    report.write(
        f"UDP Packets: {udp_count}\n"
    )

    report.write(
        f"ICMP Packets: {icmp_count}\n\n"
    )

    if connection_counts:

        report.write(
            f"Top Talker: {top_ip}\n"
        )

        report.write(
            f"Packet Count: "
            f"{connection_counts[top_ip]}\n\n"
        )

    report.write("Suspicious IPs:\n")

    suspicious_found = False

    for ip, count in connection_counts.items():

        if count > ALERT_THRESHOLD:

            suspicious_found = True

            report.write(
                f"{ip} - {count} packets\n"
            )

    if not suspicious_found:
        report.write(
            "No suspicious activity detected.\n"
        )

print(
    "\nSecurity report saved to "
    "security_report.txt"
)
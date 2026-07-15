"""
CodeAlpha Cyber Security Internship - Task 1
Basic Network Sniffer (SIMULATION VERSION)
"""
import random
import time
from datetime import datetime
# ---------- Sample / simulated network traffic ----------
# In real life, a sniffer reads this kind of info directly off the network card.
# Here we generate realistic-looking sample packets to demonstrate the analysis.
SAMPLE_PACKETS = [
    {
        "src_ip": "192.168.1.5", "dst_ip": "142.250.183.14",
        "protocol": "TCP", "src_port": 51322, "dst_port": 443,
        "flags": "PA", "payload": "GET /search?q=cybersecurity HTTP/1.1"
    },
    {
        "src_ip": "192.168.1.5", "dst_ip": "8.8.8.8",
        "protocol": "UDP", "src_port": 60112, "dst_port": 53,
        "flags": "-", "payload": "DNS Query: example.com"
    },
    {
        "src_ip": "192.168.1.5", "dst_ip": "13.107.42.14",
        "protocol": "TCP", "src_port": 51400, "dst_port": 80,
        "flags": "SYN", "payload": "GET /index.html HTTP/1.1"
    },
    {
        "src_ip": "192.168.1.5", "dst_ip": "104.18.32.7",
        "protocol": "TCP", "src_port": 51500, "dst_port": 443,
        "flags": "ACK", "payload": "TLS Handshake (encrypted data)"
    },
    {
        "src_ip": "192.168.1.5", "dst_ip": "192.168.1.1",
        "protocol": "ICMP", "src_port": None, "dst_port": None,
        "flags": "-", "payload": "Echo Request (ping)"
    },
]

COMMON_PORTS = {
    80: "HTTP (Website)",
    443: "HTTPS (Secure Website)",
    21: "FTP (File Transfer)",
    22: "SSH (Secure Remote Login)",
    25: "SMTP (Email Sending)",
    53: "DNS (Domain Name Lookup)",
    110: "POP3 (Email)",
    143: "IMAP (Email)",
}


def identify_service(dport, sport):
    """Match ports with well-known services"""
    if dport in COMMON_PORTS:
        return COMMON_PORTS[dport]
    if sport in COMMON_PORTS:
        return COMMON_PORTS[sport]
    return "Unknown / Custom Service"


def explain_data_flow(packet, packet_number):
    """
    Ek packet ka poora structure todke dikhata hai — data internet par
    kis tarah 'layers' mein wrapped hoke travel karta hai
    """
    print("=" * 65)
    print(f"[Packet #{packet_number}]  Time: {datetime.now().strftime('%H:%M:%S')}")
    print("=" * 65)

    # ---------- LAYER 3: NETWORK LAYER (IP) ----------
    print("[Network Layer - IP]")
    print(f"   Source IP      : {packet['src_ip']}")
    print(f"   Destination IP : {packet['dst_ip']}")

    # ---------- LAYER 4: TRANSPORT LAYER ----------
    protocol = packet["protocol"]
    if protocol == "TCP":
        print(f"\n[Transport Layer - TCP]  (Connection-based, reliable)")
        print(f"   Source Port      : {packet['src_port']}")
        print(f"   Destination Port : {packet['dst_port']}")
        print(f"   Flags            : {packet['flags']}")
        print(f"   Likely Service   : {identify_service(packet['dst_port'], packet['src_port'])}")

    elif protocol == "UDP":
        print(f"\n[Transport Layer - UDP]  (Connectionless, fast)")
        print(f"   Source Port      : {packet['src_port']}")
        print(f"   Destination Port : {packet['dst_port']}")
        print(f"   Likely Service   : {identify_service(packet['dst_port'], packet['src_port'])}")

    elif protocol == "ICMP":
        print(f"\n[Transport Layer - ICMP]  (Used by 'ping' / error messages)")

    # ---------- LAYER 7: APPLICATION LAYER (actual data) ----------
    print(f"\n[Application Layer - Payload / Actual Data]")
    print(f"   Data Preview : {packet['payload']}")
    print()


def main():
    print("\n" + "#" * 65)
    print("#  CodeAlpha Cyber Security - Task 1: Network Sniffer (Simulation)")
    print("#" * 65)
    print("\nSimulating packet capture...\n")
    print("Data kaise safar karta hai (data flow):")
    print("  Aapka Computer -> [IP Layer: address] -> [TCP/UDP Layer: port]")
    print("  -> [Payload: asal data] -> Internet -> Destination Computer\n")

    time.sleep(1)

    for i, packet in enumerate(SAMPLE_PACKETS, start=1):
        explain_data_flow(packet, i)
        time.sleep(0.5)  # thora delay taake "live capture" jaisa feel aaye

    print(f"Simulation complete. Total {len(SAMPLE_PACKETS)} packets analyzed.\n")
    print("NOTE: Ye sample/demo data tha. Real network traffic capture ke liye")
    print("      'scapy' library ke saath apne computer par admin/root rights")
    print("      ke sath run karna hoga: pip install scapy + sudo python3 script.py")


if __name__ == "__main__":
    main()
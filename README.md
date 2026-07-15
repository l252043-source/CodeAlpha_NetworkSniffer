# CodeAlpha_NetworkSniffer

A Python-based network sniffer that captures and analyzes network traffic, breaking down packets into IP, Transport (TCP/UDP), and Application layers to demonstrate how data flows across a network.

Built as part of the **CodeAlpha Cyber Security Internship — Task 1**.

---

## 📌 Description

This project simulates/captures network packets and analyzes their structure layer by layer, showing:
- **Network Layer (IP):** Source and destination IP addresses
- **Transport Layer (TCP/UDP/ICMP):** Ports, protocol type, and connection flags
- **Application Layer:** The actual data/payload being transmitted

The goal is to understand how data travels across a network — from one device to another — packet by packet.

---

## ✨ Features

- Captures/analyzes network packets and displays their structure
- Identifies protocol type (TCP, UDP, ICMP)
- Detects common services based on port number (HTTP, HTTPS, DNS, FTP, SSH, etc.)
- Displays source/destination IP addresses and ports
- Shows payload/data preview for each packet
- Clean, readable console output for easy analysis

---

## 🛠️ Technologies Used

- **Python 3**
- **Scapy** library (for real packet capture)

---

## 🚀 How to Run

### Requirements
```bash
pip install scapy
```

### Run the program
```bash
# Windows (Run terminal as Administrator)
py network_sniffer.py

# Linux/Mac (requires root privileges)
sudo python3 network_sniffer.py
```

> **Note:** Capturing live network packets requires administrator/root privileges, since it accesses raw network data directly.

---

## 📸 Sample Output

```
#################################################################
#  CodeAlpha Cyber Security - Task 1: Network Sniffer (Simulation)
#################################################################

Simulating packet capture...

Data kaise safar karta hai (data flow):
  Aapka Computer -> [IP Layer: address] -> [TCP/UDP Layer: port]
  -> [Payload: asal data] -> Internet -> Destination Computer

=================================================================
[Packet #1]  Time: 09:58:57
=================================================================
[Network Layer - IP]
   Source IP      : 192.168.1.5
   Destination IP : 142.250.183.14

[Transport Layer - TCP]  (Connection-based, reliable)
   Source Port      : 51322
   Destination Port : 443
   Flags            : PA
   Likely Service   : HTTPS (Secure Website)

[Application Layer - Payload / Actual Data]
   Data Preview : GET /search?q=cybersecurity HTTP/1.1

=================================================================
[Packet #2]  Time: 09:58:58
=================================================================
[Network Layer - IP]
   Source IP      : 192.168.1.5
   Destination IP : 8.8.8.8

[Transport Layer - UDP]  (Connectionless, fast)
   Source Port      : 60112
   Destination Port : 53
   Likely Service   : DNS (Domain Name Lookup)

[Application Layer - Payload / Actual Data]
   Data Preview : DNS Query: example.com

=================================================================
[Packet #5]  Time: 09:58:59
=================================================================
[Network Layer - IP]
   Source IP      : 192.168.1.5
   Destination IP : 192.168.1.1

[Transport Layer - ICMP]  (Used by 'ping' / error messages)

[Application Layer - Payload / Actual Data]
   Data Preview : Echo Request (ping)

Simulation complete. Total 5 packets analyzed.
```

📁 Full output screenshots available in this repo: `Output-part1.png`, `Output-part2.png`, `Output-part3.png`

---

## 📚 What I Learned

Through this project, I learned how data is structured and transmitted across a network using layered protocols (IP, TCP/UDP, and application data). I also gained hands-on experience with the Scapy library for packet analysis, understanding common network protocols and port-based services, and how tools like packet sniffers are used in cybersecurity for traffic monitoring and threat detection.

---

## 🎓 About CodeAlpha

This project was completed as part of the **CodeAlpha Cyber Security Virtual Internship**, which provides hands-on experience in network security, ethical hacking, and threat detection through real-world projects.

🔗 [www.codealpha.tech](https://www.codealpha.tech)

# CodeAlpha - Basic Network Sniffer

## 📌 Project Overview

This project is a Basic Network Sniffer developed using Python and Scapy as part of the CodeAlpha Cyber Security Internship.

The program captures live network packets and displays important packet information such as Source IP Address, Destination IP Address, Protocol, Source Port, Destination Port, and Payload information.

---

## 🚀 Features

- Capture live network packets
- Display Source IP Address
- Display Destination IP Address
- Detect Protocol (TCP, UDP, ICMP)
- Display Source Port and Destination Port
- Display Packet Payload Information
- Display Packet Number
- Display Current Timestamp
- Stop packet capture using CTRL + C

---

## 🛠 Technologies Used

- Python 3
- Scapy

---

## 📦 Requirements

Install the required package:

```bash
pip install -r requirements.txt
```

Or install Scapy directly:

```bash
pip install scapy
```

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/mdarif9434/CodeAlpha-Basic-Network-Sniffer.git
```

Go to the project folder:

```bash
cd CodeAlpha-Basic-Network-Sniffer
```

Run the program:

```bash
python sniffer.py
```

---

## 📷 Sample Output

```
======================================================================
Packet Number      : 1
Time               : 2026-07-30 14:05:38

Source IP          : 192.168.0.110
Destination IP     : 142.250.xxx.xxx

Protocol           : TCP

Source Port        : 52345
Destination Port   : 443

Payload            : Encrypted / Binary Data
======================================================================
```

---

## 📸 Screenshots

### Output 1

![Output 1](screenshots/output1.png.png)

### Output 2

![Output 2](screenshots/output2.png.png)

### Output 3

![Output 3](screenshots/output3.png.png)

## 📂 Project Structure

```
CodeAlpha-Basic-Network-Sniffer
│
├── sniffer.py
├── requirements.txt
├── README.md
└── screenshots
```

---

## 🎯 Learning Outcomes

This project helped me learn:

- Packet Sniffing
- Network Packet Analysis
- IP Address Analysis
- TCP/UDP Protocols
- Python Networking
- Scapy Library

---

## 👨‍💻 Author

**Md Arif Khan**

University of Global Village (UGV)

CodeAlpha Cyber Security Internship

GitHub: https://github.com/mdarif9434

---

## 📄 License

This project is created for educational purposes as part of the CodeAlpha Cyber Security Internship.

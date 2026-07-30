from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime

# ==========================
# Packet Counter
# ==========================
packet_count = 0
tcp_count = 0
udp_count = 0
icmp_count = 0

print("=" * 75)
print("           CodeAlpha Basic Network Sniffer")
print("=" * 75)
print("Developed by: Md Arif Khan")
print("Capturing Packets... Press CTRL + C to Stop\n")


def packet_callback(packet):
    global packet_count, tcp_count, udp_count, icmp_count

    packet_count += 1

    print("=" * 75)
    print(f"Packet Number      : {packet_count}")
    print(f"Time               : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    if packet.haslayer(IP):

        print(f"Source IP          : {packet[IP].src}")
        print(f"Destination IP     : {packet[IP].dst}")

        # ---------------- TCP ----------------
        if packet.haslayer(TCP):
            tcp_count += 1
            print("Protocol           : TCP")
            print(f"Source Port        : {packet[TCP].sport}")
            print(f"Destination Port   : {packet[TCP].dport}")

        # ---------------- UDP ----------------
        elif packet.haslayer(UDP):
            udp_count += 1
            print("Protocol           : UDP")
            print(f"Source Port        : {packet[UDP].sport}")
            print(f"Destination Port   : {packet[UDP].dport}")

        # ---------------- ICMP ----------------
        elif packet.haslayer(ICMP):
            icmp_count += 1
            print("Protocol           : ICMP")

        else:
            print("Protocol           : Other")

        # ---------------- Payload ----------------
        if packet.haslayer(Raw):

            raw_data = packet[Raw].load

            try:
                text = raw_data.decode("utf-8")

                printable = sum(c.isprintable() for c in text)

                if printable / max(len(text), 1) > 0.8:
                    print(f"Payload            : {text[:100]}")
                else:
                    print("Payload            : Encrypted / Binary Data")

            except:
                print("Payload            : Encrypted / Binary Data")

        else:
            print("Payload            : None")

    print("=" * 75)


try:
    sniff(
        prn=packet_callback,
        filter="ip",
        store=False
    )

except KeyboardInterrupt:

    print("\n")
    print("=" * 75)
    print("Packet Capture Stopped")
    print("=" * 75)

    print(f"Total Packets      : {packet_count}")
    print(f"TCP Packets        : {tcp_count}")
    print(f"UDP Packets        : {udp_count}")
    print(f"ICMP Packets       : {icmp_count}")

    print("=" * 75)
    print("Thank you for using CodeAlpha Basic Network Sniffer")
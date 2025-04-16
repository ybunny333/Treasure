
from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

def main():
    print("Starting packet sniffer... (Press Ctrl+C to stop)")
    sniff(prn=packet_callback, store=False)

if __name__ == "__main__":
    main()

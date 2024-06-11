from scapy.all import *

PROTOCOLS = {
    
    1: "ICMP",
    6: "TCP",
    17: "UDP"
}


def sniffer(interface="wlp4s0"):
    sniff(iface=interface, prn=process_packet, count=100)


def process_packet(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src 
        dst_ip = packet[IP].dst 
        print("-----------------------------------------------------")
        print(f"Source: {src_ip} --> Destination: {dst_ip}")
       
        prot_num = packet[IP].proto 
        prot_name = PROTOCOLS.get(prot_num, "Unknown")
        print(f"    Protocol: {prot_name}")
        print("-----------------------------------------------------")


if __name__ == '__main__':
    sniffer()




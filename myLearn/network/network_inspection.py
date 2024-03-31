from scapy.all import sr1, IP, UDP, DNS, DNSQR, TCP


def learn_dns_query(destination_ip):
    # Craft a DNS query packet
    packet = IP(dst=destination_ip) / UDP(dport=53) / DNS(qd=DNSQR(qname='baidu.com'))
    # Send the packet
    response = sr1(packet, verbose=0)
    # Check if a response was received
    if response:
        # The DNS layer and its fields can be accessed like this
        dns_layer = response.getlayer(DNS)

        print("Received DNS response from: {}".format(response[IP].src))
        print("DNS query answered by server: {}".format(dns_layer.ns))
        print("Answers:")
        for i in range(dns_layer.ancount):
            print(dns_layer.an[i].rrname, dns_layer.an[i].rdata)
    else:
        print("No response received.")


def learn_tcp_redirect(source_subnet, destination_ip, destination_port=80):
    # Craft a TCP packet from the source_subnet to the destination_ip:destination_port
    packet = IP(src=source_subnet, dst=destination_ip) / TCP(dport=destination_port)
    # Send the packet
    response = sr1(packet, verbose=0)
    return response

if __name__ == "__main__":
# Replace '192.168.1.1' with your actual destination IP
    learn_dns_query('114.114.114.114')
# Replace '192.168.3.100' with an IP in your source subnet and '192.168.1.1' with your destination IP
#     print(learn_tcp_redirect('192.168.3.100', '110.242.68.66'))

import threading
import os
import re
from  concurrent.futures import ThreadPoolExecutor

received_packages = re.compile(r"Received[\s]*=[\s]*(?P<n>[0-9]+)")
status = ("no response", "alive but losses", "alive")


def ip_check(ip):
    ping_out = os.popen("ping -n 2 "+ip, "r")
    successful_pings = 0
    while True:
        line = ping_out.readline()
        if not line:
            break
        n_received =received_packages.search(line)
        
        if n_received:
            successful_pings = int(n_received.group('n'))
    print(f'ping {ip} received package {successful_pings}')
    



def ip_create(range):
    return ("192.168.1." + str(suffix) for suffix in range)

ips = tuple(ip_create(range(1,8)))

with ThreadPoolExecutor(max_workers=4) as t:
    t.map(ip_check,ips)


# check_results = []
# for suffix in range(1, 70):
#    ip = "192.168.1."+str(suffix)
#    current = ip_check(ip)
#    check_results.append(current)
#    current.start()

# for el in check_results:
#    el.join()
#    print("ping ", el.ip, "received package ", el._successful_pings)

import threading
import os
import re
from  concurrent.futures import ThreadPoolExecutor

received_packages = re.compile(r"Received[\s]*=[\s]*(?P<n>[0-9]+)")
status = ("no response", "alive but losses", "alive")


class ip_check(threading.Thread):
   def __init__(self, ip):
      threading.Thread.__init__(self)
      self.ip = ip
      self._successful_pings = -1

   def run(self):
      ping_out = os.popen("ping -n 2 "+self.ip, "r")
      while True:
        line = ping_out.readline()
        if not line:
           break
        n_received =received_packages.search(line)
        if n_received:
           self._successful_pings = int(n_received.group('n'))

   def status(self):
      if self._successful_pings == 0:
         return "no response"
      elif self._successful_pings == 1:
         return "alive, but 50 % package loss"
      elif self._successful_pings == 2:
         return "alive"
      else:
         return "shouldn't occur"



check_results = []
for suffix in range(1, 70):
   ip = "192.168.1."+str(suffix)
   current = ip_check(ip)
   check_results.append(current)
   current.start()

for el in check_results:
   el.join()
   print("ping ", el.ip, "received package ", el._successful_pings)

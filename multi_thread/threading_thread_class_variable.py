import threading
prime_qty = 0

class PrimeNumber(threading.Thread):
  def __init__(self, number):
    threading.Thread.__init__(self)
    self.Number = number

  def run(self):
    global prime_qty
    counter = 2
    
    while counter*counter <= self.Number:
        if self.Number % counter == 0:
            print (f"{self.Number} is no prime number, because {self.Number} = {counter} * {int(self.Number / counter)}")
            return
        counter += 1 
    print (f"{self.Number} is a prime number")
    prime_qty = prime_qty + 1


threads = [] 
in1 = 100
while True: 
    # in1 = int(input("number: "))
    
    # in1 = int(in1)
    if in1 < 1: 
        break 
 
    thread = PrimeNumber(in1) 
    threads.append(thread)
    thread.start() 
    # thread.join()
    in1 = in1 -1
 
for x in threads:
    x.join()

print(prime_qty)

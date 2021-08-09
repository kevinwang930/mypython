import threading


class PrimeNumber(threading.Thread):

    prime_numbers = {}
    lock = threading.Lock()

    def __init__(self, number):
        threading.Thread.__init__(self)
        self.Number = number
        PrimeNumber.lock.acquire()
        PrimeNumber.prime_numbers[number] = "None"
        PrimeNumber.lock.release()

    def run(self):
        counter = 2
        res = True
        while counter*counter <= self.Number:
            if self.Number % counter == 0:
                res = False
            counter += 1
        PrimeNumber.lock.acquire()
        PrimeNumber.prime_numbers[self.Number] = res
        PrimeNumber.lock.release()


threads = []
while True:
    in1 = int(input("number: "))
    # in1 = int(in1)
    if in1 < 1:
        print(f'prime numbers {PrimeNumber.prime_numbers}')
        break

    thread = PrimeNumber(in1)
    threads.append(thread)
    thread.start()

for x in threads:
    x.join()


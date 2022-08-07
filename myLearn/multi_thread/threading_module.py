import time
from threading import Thread,get_native_id


def sleeper():
    print (f"thread id {get_native_id()} sleeps for 5 seconds")
    time.sleep(5)
    print(f"thread id {get_native_id()} wake up")


for i in range(10):
    t = Thread(target=sleeper)
    t.start()

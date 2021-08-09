from time import time,sleep
from multiprocessing import Pool
from os import getpid


def f(x):
    sleep(2)  # Wait 2 seconds
    print(x*x)

print(f'current process id {getpid()}')
# t0 = time()
# for item in [1, 2, 3, 4]:
#     f(item)
# t1 = time() - t0
# print(f'time elapsed {t1}')
if __name__ == '__main__':
    t0 = time()
    p = Pool(2)
# with Pool(4) as p:
    p.map(f, [1, 2, 3, 4])
    p.close()
    p.join()
    t1 = time() - t0
    print(f'time elapsed {t1}')

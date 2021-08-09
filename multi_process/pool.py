from multiprocessing import Pool
from time import time, sleep

def f(x):
    sleep(2)
    y = x*x
    print(y)
    # return y


# t0 = time()
# for item in [1, 2, 3, 4]:
#     f(item)
# t1 = time() - t0
# print(f'time elapsed {t1}')

if __name__ == '__main__':
    tp0 = time()
    with Pool(3) as p:
        p.map(f, [1, 2, 3])
    tp1 = time() - tp0
    print(f'elapsed time {tp1}')

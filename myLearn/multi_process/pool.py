import os
from multiprocessing import Pool
from time import time, sleep
from datetime import datetime
def f(folder):

    path = os.path.join('/code/git',folder)
    out =os.popen(f'cd {path}&&git status')
    # print(out.read())
    sleep(3)
    print(datetime.now())
    # return y


# t0 = time()
# for item in [1, 2, 3, 4]:
#     f(item)
# t1 = time() - t0
# print(f'time elapsed {t1}')

if __name__ == '__main__':
    with Pool(5) as p:
        p.map(f, os.listdir('/code/git'))


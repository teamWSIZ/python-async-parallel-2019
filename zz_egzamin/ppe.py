import multiprocessing as mp
import os
import threading
from concurrent.futures.process import ProcessPoolExecutor
from time import sleep
from typing import List, Dict


def t():
    return threading.current_thread().name


def task(arg, scena: List[int], mapa: Dict):
    print(
        f'start task [{arg}] scena:{scena, id(scena)} '
        f'wątek: {t()} proces:{os.getpid()} '
        f'mapa[one]: {mapa["one"]}')
    scena[0] = 100
    if arg == 0:
        mapa['one'] = 1
    sleep(4)
    print(f'koniec task [{arg}]')
    return arg


if __name__ == '__main__':
    print(f'start programu')
    man = mp.Manager()
    d = man.dict()
    d['one'] = -1

    executor = ProcessPoolExecutor(4)
    ff = []
    data = [1, 1, 0, 0]

    for i in range(4):
        future_result = executor.submit(task, i, data, d)
        ff.append(future_result)
        print(f'submitted {i}')

    zzz = 0.00001
    sleep(zzz)  # początkowy przestój
    data[3] = 111

    print(f'koniec programu')

    suma = 0
    for f in ff:
        suma += f.result()
    print(f'suma: {suma}')

from concurrent.futures.process import ProcessPoolExecutor
from time import sleep
from typing import List
import multiprocessing as mp


def render_scene(arg, scena: List[int]):
    """
    """
    print(f'start task [{arg}] scena:{scena, id(scena)}')
    sleep(0.3)
    print(f'koniec task [{arg}]')
    return arg * arg


man = mp.Manager()
mapa = man.dict()  # dict shared between processes

if __name__ == '__main__':
    executor = ProcessPoolExecutor()
    for i in range(5):
        executor.submit(render_scene, i, [])

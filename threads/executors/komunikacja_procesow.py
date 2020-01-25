from concurrent.futures.process import ProcessPoolExecutor
from time import sleep
from typing import List, Dict
import multiprocessing as mp


def render_scene(arg, scena: List[int], mapa: Dict):
    """
    """
    print(f'start task [{arg}] scena:{scena, id(scena)}')
    sleep(0.3)
    print(f'koniec task [{arg}], value={mapa["xxx"]}')
    mapa['xxx'] = arg
    return arg * arg



if __name__ == '__main__':
    man = mp.Manager()
    mapa = man.dict()  # dict shared between processes
    mapa['xxx'] = -1
    executor = ProcessPoolExecutor()
    for i in range(5):
        executor.submit(render_scene, i, [], mapa)

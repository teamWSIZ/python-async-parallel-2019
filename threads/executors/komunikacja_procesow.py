from concurrent.futures.process import ProcessPoolExecutor
from time import sleep
from typing import List, Dict
import multiprocessing as mp


def render_scene(arg, scena: List[int], mapa: Dict):
    """
    """
    # print(f'start task [{arg}] scena:{scena, id(scena)}')
    sleep(0.3)
    if arg % 1 == 0:
        print(f'koniec task [{arg}], mapa[xxx]={mapa["xxx"]},  qu={shared_que.qsize()} '
              f'val={shared_val.value}')
    mapa['xxx'] = arg
    shared_que.put(arg, False)
    shared_val.value += 1
    return arg * arg


if __name__ == '__main__':
    # tworzenie struktur danych współdzielonych między procesami
    man = mp.Manager()
    mapa = man.dict()  # (działa jak dict, ale wysyła informacje między procesami)
    mapa['xxx'] = -1
    shared_que = mp.Queue(maxsize=1200)  # kolejka typu FIFO
    shared_val = mp.Value('i', 0)  # pojedyncza wartość

    executor = ProcessPoolExecutor(48)
    for i in range(20):
        executor.submit(render_scene, i, [], mapa)
    sleep(10)

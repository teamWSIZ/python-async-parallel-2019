import threading
from concurrent.futures._base import Future
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor
from dataclasses import dataclass
from time import sleep
from typing import List
import os


def t():
    return threading.current_thread().name


global_d = 112


@dataclass
class MyConfig:
    id: int
    starting_position: int


def render_scene(arg, scena: List[int], config: MyConfig):
    print(f'start {arg, scena, id(scena)}, wątek: {t()} proces:{os.getpid()} -> {global_d}, {id(global_d)}')
    scena[0] = 100
    sleep(0.3)
    print(f'end {arg}')
    return arg * arg


if __name__ == '__main__':
    TASK_COUNT = 30

    print(f'start programu, adres global_d:{id(global_d)}')

    executor = ProcessPoolExecutor(10)  # single physical thread; async
    future_results: List[Future] = []
    common_scene = [1, 1, 0, 0, 1]

    for i in range(TASK_COUNT):
        config = MyConfig(i, 5 + i)
        # wrzuca zadanie do wykonania; nie czeka na wynik
        future_result = executor.submit(render_scene, i, common_scene, config)
        future_results.append(future_result)
        print(f'submitted {i}')

    sleep(0.1)
    global_d = 0  # nie wplynie na zasubmitowane zadania    sleep(0.1)
    sleep(0.1)

    executor.submit(render_scene, -1, common_scene, MyConfig(0, 0))
    print(f'konice programu, adres global_d:{id(global_d)}')

    suma = 0
    for f in future_results:
        suma += f.result()
    print(f'suma: {suma}')

import threading
from concurrent.futures._base import Future
from concurrent.futures.thread import ThreadPoolExecutor
from time import sleep
from typing import List


def t():
    return threading.current_thread().name


def zadanie(arg):
    print(f'wykonuję zadanie {arg}, wątek: {t()}')
    sleep(2.0)
    return arg * arg


def print_futures_done(futures: List[Future]):
    for fu in futures:
        if fu.done():
            print(1, end='')
        else:
            print(0, end='')
    print()


executor = ThreadPoolExecutor(4)  # single physical thread; async

future_results: List[Future] = []

for i in range(12):
    future_result = executor.submit(zadanie, i)  # wrzuca zadanie do wykonania; nie czeka na wynik
    future_results.append(future_result)
    print(f'submitted {i}')

for i in range(20):
    print_futures_done(future_results)
    sleep(1)

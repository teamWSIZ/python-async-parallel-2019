import threading
from concurrent.futures._base import Future
from concurrent.futures.thread import ThreadPoolExecutor
from time import sleep
from typing import List


def t():
    return threading.current_thread().name


def zadanie(arg):
    print(f'wykonuję zadanie {arg}, wątek: {t()}')
    sleep(0.3)
    return arg * arg


def print_futures_done(futures: List[Future]):
    """
    Funkcja bierze listę obiektów typu Future, i (zaczynając 'od lewej')
    wypisuje 1 jeśli dany Future ma flagę 'done', lub 0 jeśli nie ma flagi done.

    Uwaga:
    """
    for fu in futures:
        if fu.done():
            if fu.cancelled():
                print('x', end='')
            else:
                print(1, end='')
        else:
            print(0, end='')
    print()


if __name__ == '__main__':
    """
    Funkcja startowa (przydaje się, jeśli zamiast uruchamiać ten file, chcemy go include-ować)
    """
    executor = ThreadPoolExecutor(4)  # single physical thread; async
    future_results: List[Future] = []

    for i in range(12):
        future_result = executor.submit(zadanie, i)  # wrzuca zadanie do wykonania; nie czeka na wynik
        future_results.append(future_result)
        if i == 10:
            future_results[9].cancel()  # przykład z usunięciem zaplanowanego zadania
        print(f'submitted {i}')

    for i in range(15):
        print_futures_done(future_results)
        sleep(0.5)

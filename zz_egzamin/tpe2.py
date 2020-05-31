import threading
from concurrent.futures.thread import ThreadPoolExecutor
from time import sleep, time


def t():
    return threading.current_thread().name


def zadanie(i):
    sleep(i * 0.1)
    return i


ex = ThreadPoolExecutor(200)
futures = []
start = time()
for i in range(101):
    futures.append(ex.submit(zadanie, i))

print(f'zadania zasubmitowane, {time()-start}s')
futures[0].result()
print(f'punkt 1, {time()-start}s')
r = 0
for f in futures:
    r += f.result()
print(f'punkt 2, {time()-start}s')
print(r)
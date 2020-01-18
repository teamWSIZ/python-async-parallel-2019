from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor
from time import sleep
import os
import multiprocessing as mp


# use watch -n1 'ps ax | grep python'
# check more on: https://docs.python.org/3/library/multiprocessing.html#sharing-state-between-processes


class Container:
    www = '.'


# struktury share'owane mi
cont = Container()
qq = mp.Queue()
man = mp.Manager()
mapa = man.dict()  # dict shared between processes
# lista = man.list()
# ll = man.Lock()


def zadanie(arg: float):
    print(f'zaczynam: {arg} {cont.www} [{os.getpid()}]')
    sleep(arg)
    cont.www += str(arg)
    qq.put(arg)
    if 'p1' in mapa:
        print('meh...')
    mapa[f'p{arg}'] = arg * arg
    print(f'kończę: {arg} {cont.www}, q{qq.qsize()}')


# ex = ThreadPoolExecutor(4)
ex = ProcessPoolExecutor(4)
f1 = ex.submit(zadanie, 2)
f2 = ex.submit(zadanie, 1)
f3 = ex.submit(zadanie, 3)

# f3.add_done_callback(lambda a: print('ok'))
f3.result()

f4 = ex.submit(zadanie, 8)
print(f'--> {cont.www}')

print(mapa)

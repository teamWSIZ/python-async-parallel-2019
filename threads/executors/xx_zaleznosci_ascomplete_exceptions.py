from concurrent.futures import as_completed, ThreadPoolExecutor
from time import sleep


def zadanie(arg):
    print(f'wykonuję zadanie {arg}, wątek: {t()}')
    sleep(2.0 + 2 * arg)
    if arg == 3:
        raise Exception('meh...')
    return arg * arg


ex = ThreadPoolExecutor(4)
w1 = ex.submit(zadanie, 4)
sleep(0.7)
w2 = ex.submit(zadanie, 3)
print('zadania za-submit-owane')

# for f in as_completed({w1, w2}):
#     pętla w kolejności w jakiej te 'future's się kończą (ważne!!)
# print(f'result:{f.result()}')

print('--------------')
# value1 = w1.result()
print(f'mam wynik zadania dla 4')
# value2 = w2.result()
print(f'mam wynik zadania dla 3')

# zjedzone wyjątki...

# ttt = ex.submit(zadanie, value1 + value2)
# print(f'ostateczny wynik to: {ttt.result()}')

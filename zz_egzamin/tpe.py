import threading
from concurrent.futures.thread import ThreadPoolExecutor
from time import sleep


def t():
    return threading.current_thread().name

def foo(i):
    print(f'zadanie {i} wątek {t()}')
    sleep(0.0001)
    return i*i

ex = ThreadPoolExecutor(16)
f1 = ex.submit(foo, 5)
f2 = ex.submit(foo, 5)
print(t())
sleep(0.000001)
# w = f1 + f2

f2.result() # ... ?

print(f2.done())

f2.cancel()
print(f'--> {f2.cancelled()}')


# czy program można uruchomić z ThreadPoolExecutor(16) na 2-core'owym CPU ?
# czy wątek który wykona zadanie to zawsze będzie `ThreadPoolExecutor-0_0`
# czy (komunikat z) 'MainThread' jest zawsze po 'ThreadPoolExecutor-0_'
# jaki będzie efekt odkomentowania linii liczącej `f1 + f2`
# co zrobić by zebrać wyniki z wykonania f1 i f2 ?
# z f2.done() zawsze wyjdzie "True"
# f2.result() powoduje, że MainThread czeka aż egzekutor skończy wykonanie funkcji z f2
# f2.result() --- może mieć wartość True lub False
#Q: napisanie f2.cancel() po f2.done()
# - spowoduje błąd systemowy (bo f2 już jest done, i nie można jej zatrzymać)
# - spowoduje, że następne wywołanie f2.cancelled() da True
# - zwróci "0" jeśli zadanie udało się zatrzymać, lub błąd jeśli już zostało wykonane






# Wykonanie powyższego programu:
# - wypisze nazwę aktualnego wątku
# - wypisze 'MainThread'
# - nie wypisze niczegow




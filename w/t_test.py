import threading
import time


class Pracownik(threading.Thread):
    def __init__(self, x):
        threading.Thread.__init__(self)
        self.x = x

    def run(self):
        print(f'x={self.x} wątek:{threading.current_thread().name}')

thread1 = Pracownik(1)
thread2 = Pracownik(2)
thread1.start()
threading.current_thread().name
thread1.join()
thread2.start()
threading.current_thread().name
thread2.join()


# t = []
# for i in range(200):
#     tt = Pracownik(i)
#     tt.start()
#     t.append(tt)


# thread3.start()
#
# thread1.join()
# thread2.join()
# thread3.join()
#
# print(threading.current_thread().name)
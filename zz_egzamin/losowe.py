from random import randint, random

def foo():
    w = 0
    for i in range(100):
        w += randint(0, 10)
    if w > 980:
        print(w)



print(random())
cnt = 0

for i in range(100000):
    if random() < 0.1:
        cnt += 1

# ile średnio będzie wynosiła zmienna cnt po wykonaniu programu?
# 1000
# 10000
# 100


# na koniec wykonania programu, jakie mogą być możliwe wartości `w`?
# 0 ?
# 990 ?
# 1000 ?



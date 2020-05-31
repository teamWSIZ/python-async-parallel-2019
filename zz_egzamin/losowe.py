from random import randint, random, normalvariate

def foo():
    w = 0
    for i in range(100):
        w += randint(0, 10)
    if w > 980:
        print(w)



print(random())
cnt = 0

# for i in range(1000):
#     if random() < 0.1:
#         cnt += 1

for i in range(100):
    u = normalvariate(0,1)
    print(u)


# ile średnio będzie wynosiła zmienna cnt po wykonaniu programu?
# 1000
# 10000
# 100


# na koniec wykonania programu, jakie mogą być możliwe wartości `w`?
# 0 ?
# 990 ?
# 1000 ?


w = 0
for i in range(100):
    w += randint(0, 10)
print(w)
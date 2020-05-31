from random import randint

s = set()
for i in range(10000):
    s.add(randint(0, 10))

print(s)

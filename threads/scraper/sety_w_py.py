import time
from random import randint
import random

# set zbiera unikalne elementy:
from typing import List

random.seed(137)

s = set()
s.add(14)
s.add(11)
s.add(54)
s.add(11)
print(s)  # {54, 11, 14}


def get_unique_list(a: List[int]) -> List[int]:
    uniq = []
    for x in a:
        if x not in uniq:
            uniq.append(x)
    return uniq

def get_unique_set(a: List[int]) -> List[int]:
    uniq = set()
    for x in a:
        uniq.add(x)
    # return uniq
    # trzeba zamienic na liste
    return [e for e in uniq]

# zbior 100tys losowych liczb
a = [randint(0, 1000000) for _ in range(10)]


print(a)
start = time.time()
# uu = get_unique_list(a)
uu = get_unique_set(a)
end = time.time()

print(f'czas:{end-start:.3f}s  elementow:{len(uu)}')

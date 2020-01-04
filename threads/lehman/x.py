from dataclasses import dataclass

w = [1, 2, 3, 0]


# print(w.__len__())
# print(w[-1])


# for i in range(10):
#     if i % 2 == 0:
#         print(i)

# sort(w)

# w.sort()

#
# def greet_user(u: str):
#     print(f'Hello {u}! Nice to meet you!')
# greet_user(4)

@dataclass
class A:
    x: int
    y: int


a = A(x=12, y=13)
b = A(x=12, y=13)

print(a == b)
print(a is b)
a.x = 10
print(b.x)


class Flower:
    x: int


class Rose(Flower):
    y: int

r = Rose()
r.x = 12

z: Flower = r


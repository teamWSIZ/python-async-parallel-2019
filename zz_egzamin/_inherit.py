from typing import List


class A:
    x: int

    def __init__(self, x):
        print('creating A')
        self.x = x

    def foo(self):
        self.x += 1


class B(A):
    y: int

    def __init__(self, y):
        super().__init__(2 * y)
        self.y = y

    def goo(self):
        self.foo()

    def foo(self):
        self.x -= 1


a = A(1)
b = B(1)
w: List[A] = [a, b]

b.goo()
print(b.x)

# print(b.c)
#
# print(b.x)
# for r in w:
#     print(r.x)


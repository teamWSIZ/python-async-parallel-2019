from dataclasses import dataclass, asdict

# w = W(5, 'abc')
# print(w)
#
# W()
# print(asdict(W(5,'a')))


@dataclass
class W:
    a: int
    b: str

g = {'a': 5, 'b': 'a'}
# print(type(g))

class G:
    def __init__(self, a, b):
        self.a = a
        self.b = b

print(G(1,2).__dict__)

print(g['a'])

x = W(**g)
print(x)
print(x.a)

print(g.items())
import copy

x = 11
y = 12

print(f'adres x: {id(x)}')
print(f'adres y: {id(y)}')

z = x
print(f'adres z: {id(z)}')
z = 10
print(x)
print(f'adres z: {id(z)}')

w = [1, 2, 3]
print(f'adres w{id(w)}')
u = w
print(f'adres u{id(u)}')
u[0] = 111
print(w)

t = [111, 2, 3]
print(t == w)  # True
print(t is w)  # False
print(u is w)  # True

v = copy.copy(u)    # skopiuje wszystkie elementy zmiennej `u` per value
v = copy.deepcopy(u)    # skopiuje wszystkie elementy proste, a na skomplikowanych (typu List) odpali znowu deepcopy()

print(u is v)  # False

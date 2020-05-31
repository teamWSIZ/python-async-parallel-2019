import copy

x = 11
print(f'adres x: {id(x)}')  # 93865980073056

z = x
print(f'adres z: {id(z)}')  # 93865980073056
z = 10  # przypisuje pod nowy adres
print(x)  # 11
print(f'adres z: {id(z)}')  # 93865980073024

w = [1, 2, 3]
print(f'adres w: {id(w)}')  # 140503198953952
u = w
print(f'adres u: {id(u)}')  # 140503198953952
u[0] = 111
print(w)  # [111, 2, 3]

t = [111, 2, 3]
print(t == w)  # True
print(t is w)  # False
print(u is w)  # True

v = copy.copy(u)  # skopiuje wszystkie elementy zmiennej `u` per value
v = copy.deepcopy(u)  # skopiuje wszystkie elementy proste, a na skomplikowanych (typu List) odpali znowu deepcopy()

print(u is v)  # False

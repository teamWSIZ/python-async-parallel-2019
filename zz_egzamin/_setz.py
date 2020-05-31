w = [1, 2, 3]
s = set(w)
r = {1, 2, 3}


print(type(s))
print(2 in w)
print(2 in r)
print(len(s))
# print(s.size())

print(s == r)
print(s is r)

r.add(2)
print(r)
x = "Hello,world!"
print(type(x))
print(str(x))

y = 10
print(type(y))
print(int(y))

z = 5.0
print(type(z))
print(float(z))

a = 1j
print(type(a))
print(complex(a))

b = ["red", "blue", "yellow"]
print(type(b))
print(list(b))

c = ("dark", "light")
print(type(c))
print(tuple(c))

d = range(4)
print(type(d))
print(d)

e = {"Color" : "yellow", "theme" : "light"}
print(type(e))
print(dict(e))

f = {"apple", "orange", "cherry"}
print(type(f))
print(set(f))

g = frozenset(("apple", "orange", "cherry"))
print(type(g))
print(frozenset(g))

h = True
print(type(h))
print(bool(h))

j = b'Hello'
print(type(j))
print(bytes(j))

k = bytearray(3)
print(type(k))
print(bytearray(k))

l = memoryview(bytes(5))
print(type(l))
print(l)

m = None
print(type(m))
print(m)
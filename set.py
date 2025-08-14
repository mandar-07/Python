a =set([2,3,556,])
print(a)
b={1,2,3,4,5,6,7,8,9}
print(b)
d = frozenset({"apple", "banana", "cherry"})
a.add(68)
print(a)
a.copy()
print(a)
a.clear()
print(a)
a.add(2)
a.add(3)
a.add(4)
print(b.difference(a))
print(a.union(b))





a=set()
b={1,2,3,4,11,55}
c=set([1,2,3,4])
print("printing sets",b)
print(type(b))
print(type(a))
print(type(c))


#union, intersection

d=set(range(11,20))
(d.add(55))
print(d)
e=set()
e=d.union(b)
print(e)
f=set()
f=d.intersection(b)
print(f)

g=set()
g=d.difference(b)
print(g)
# e={}
# print(e,type(e))

# e={1,2,3,4}
# print(e,type(e))

# y={1,3.2,"hello",('ho',2.3)}
# print(y,type(y))

# k={1,2,3,4}
# print(k[2])

# y={2,4,6,8}
# y=[2,4,6,8]
# print(y,type(y))
# h=frozenset(y)
# print(h)
# print(h[2]) #frozenset' object is not subscriptable

# a={1,2,3,4}
# b='hello',2.4
# a.add(b)
# print(a)

# n={2,3,4}
# n.clear()
# print(n)

# a={1,2,3,}; b={4,3,3,5}; c={10,15,6}; d=(1,4,7)
# print(a.intersection(b))
# print(a.intersection(c))
# print(a.intersection(d))
# print(b.intersection(d))
# print(b.intersection(c))
# print(c.intersection(d))

# a={1,2,3}
# b={4,3,5}
# print(a.union(b))
# print(b.union(a))

# a={1,2,3}
# b={4,3,5}
# c={5,6,7}
# a.update(b)
# print(a)
# a.update(c)
# c.update(a)
# print(c)

# a={5,10,20,25,30}
# b={10,21,5}
# print(a.difference(b)) 
# print(b.difference(a)) 
# print(a-b)
# print(b-a)

# z={55,56,57,73,45,23}
# z.discard(4)
# print(z)
# z.discard(73)
# print(z)

# v={26,7,11,4,23}
# v.pop()
# print(v)

# A={1,2,3,4}
# B={5,6,7}
# C={5,3,9}
# print('Are A and B disjoint?', A.isdisjoint(B))
# print('Are A and C disjoint?', A.isdisjoint(C))
# print('Are B and C disjoint?', B.isdisjoint(C))

# A = {1, 2, 3}
# B = {1, 2, 3, 4, 5}
# C = {1, 2, 4, 5}
# print(A.issubset(B))
# print(B.issubset(A))
# print(A.issubset(C))
# print(C.issubset(B))
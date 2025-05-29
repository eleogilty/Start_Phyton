#SET
#CREATE
a = {1, 1.2, 'hello'}
a = {}
b = set()
c = frozenset()
a = {1, 1.1, 'a', (1, 1.1), None, True, print}
a = {1, 1.1, [1, 2]}
a = frozenset ({1, 1.1})
a = [1, 'abc' , 1]
set(a)
b = set('слово')
c = frozenset('hello')
d = set([1, [2.1], 1])
a = {1, 1.1 'a'}
a.add('привет!')
b = 1
a.add(b)
a = {1, 2, 3}
a.update({5, 2})
a = {1, 1.1 'a'}
a[0]
a = {1,1.1, 'a'}
a = [0] = 'a'
a ={ 1, 2, 3}
a = {1, 1.1 'a'}
del a[0]
del a
a = {1, 2, 3}
a.clear()
a = {1, 2, 3, 4}
a.pop()
a.remove(3)
a.discard(5)
a = {1, 2, 3}
b = {3, 5, 6}
c = a-b
print(c)
a -= b
help(set)
a = {1, 2, 3}
a.copy()
a.isdisjoint({4, 5, 6})
a.issubset({4, 3, 1, 2})
a.issubset({2, 1})

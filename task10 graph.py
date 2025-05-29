print(f'задача 1')
from itertools import permutations
table = '457 567 45 136 123 247 126'.split()
graph = 'EF FA AB BG GE EC CB CD DF DA'.split()
print(*range(1, 8))
for p in permutations('ABCDEFG'):
     if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
        print(*p)

print(f'задача 2')
from itertools import permutations
table = '234 157 147 138 268 58 23 456'.split()
graph = 'DG GA AF FH HC CB BD GF EH ED EB'.split()
print(*range(1, 9))
for p in permutations('ABCDEFGH'):
     if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
        print(*p)


print(f'задача 3')
from itertools import permutations
table = '268 134678 257 27 38 12 234 125'.split()
graph = 'АГ ГБ БД ДИ ИЖ ЖЕ ЕВ ВА ВГ ГД ГИ ГЕ'.split()
print(*range(1, 9))
for p in permutations('АБВГДЕЖИ'):
     if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
        print(*p)


print(f'задача 4')
from itertools import permutations
table = '47 345 27 1267 268 458 134 56'.split()
graph = 'АБ БГ ГД ДИ ИЖ ЖЕ ЕВ ВА АГ ГЕ ДЖ'.split()
print(*range(1, 9))
for p in permutations('АБВГДЕЖИ'):
     if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
        print(*p)

print(f'задача 5')
from itertools import permutations
table = '23467 1356 12458 13 238 127 16 35'.split()
graph = 'AB BD DE EF FG GH HC CA BC CD CG DG GE'.split()
print(*range(1, 9))
for p in permutations('ABCDEFGH'):
     if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
        print(*p)

print(f'задача 6')
from itertools import permutations
table = '247 148 578 126 38 47 136 235'.split()
graph = 'AB BH HF FD DC CE EA AH FG GE GC'.split()
print(*range(1, 9))
for p in permutations('ABCDEFGH'):
     if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
        print(*p)

print(f'задача 7')
from itertools import permutations
table = '347 3456 1245 1237 236 62 14 '.split()
graph = 'BA AD DF FG GE EC CB CA CD DE EF'.split()
print(*range(1, 8))
for p in permutations('ABCDEFG'):
     if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
        print(*p)

print(f'задача 8')
from itertools import permutations
table = '279 13789 2578 57 3468 589 1234 2356 126'.split()
graph = 'АБ БЖ ЖК КЗ ЗД ДА АВ АГ ВГ ВЖ ВЕ ГЕ ЖЕ ЗЕ КЕ ГД'.split()
print(*range(1, 10))
for p in permutations('АБВГДЕЖЗК'):
     if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
        print(*p)

print(f'задача 9')
from itertools import permutations
table = '457 37 267 1678 16 3458 12348 467'.split()
graph = 'АБ БД ДЕ ЕЗ ЗГ ГА АВ ВД ДЖ ЖГ ЖВ ЕГ'.split()
print(*range(1, 9))
for p in permutations('АБВГДЕЗЖ'):
     if all(str(p.index(b) + 1) in table[p.index(a)] for a, b in graph):
        print(*p)

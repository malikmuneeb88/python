# ITERABLE : A thing we can iterate over
#ITERATOR : A special object with next() method.

import itertools

x = [1, 2, 3, 4]      # Iterable

for i in x:
    print(i)

n = itertools.cycle(x)       # Iterator

print(next(n))
print(next(n))
print(next(n))
print(next(n))
# Piotr Walędzik

# Powerset - Napisz kod tworzęcy ze zbioru A = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# zbiór zawierający wszystkie podzbiory A (włącznie z pustym i A).
# UWAGA: w python zbiory (set) nie mogą być elementami innych zbiorów,
# proszę użyć frozenset jako zbiorów wewnętrznych.
# Wynik przypisz na zmienną result
 
A = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
result = set()
 
from itertools import chain, combinations
 
for i in chain.from_iterable(combinations(A, r) for r in range(len(A)+1)):
    print(i)
    result.add(frozenset(i))
 
 
assert frozenset((0, 1, 2, 3, 4, 5, 6, 7, 8, 9)) in result
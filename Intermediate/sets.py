#sets : unordered , mutable , no duplicates

from attr import frozen


myset = {1,2,3}

print(type(myset))

myset_1 = set([2,3,4,6.5])

print(myset_1)

emp_set = set()

emp_set.add(1)

print(emp_set)

emp_set.add(2)

print(emp_set)

odds = {1,3,5,7,9}

evens = {2,4,6,8,0,10}

primes = {2,3,5,7}

un = odds.union(evens)

print(un)

inter = evens.intersection(primes) 

print(inter)

diff = odds.difference(primes)

print(diff)

sym_diff = odds.symmetric_difference(primes)

print(sym_diff)

froz_set = frozenset([2,3,4,5]) # changing set to immutable

# froz_set.add(2) #gives error because its frozen

print(froz_set)
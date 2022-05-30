from itertools import combinations_with_replacement, product,permutations,combinations

a =  [1,2]
b = [3,4]
prod = product(a,b) # calculates cartesian product

print(prod , list(prod))

perm = permutations(a)
print(perm, list(perm))
perm = permutations(b)
print(list(perm))


a = [1,2,3,4]
comb = combinations(a,2)
print(list(comb))
comb_rep = combinations_with_replacement(a,3)
print(list(comb_rep))

from itertools import accumulate

acc = [1,2,3,4]

ac = accumulate(acc)

print(list(ac)) #prints the accumulated sum of the list

import operator 

acc = [5,2,4,10,3]

ac  = accumulate(acc,func=max) # gets maximum of the array to the end

print(list(ac))

from itertools import groupby

persons = [{"name":"KAd", 'age':10}, {'name':"SAmm", 'age':12},
            {"name":"xaad", 'age':10}, {'name':"qqmm", 'age':12}]

group_obj = groupby(persons,key = lambda x: x['age'])

for key,value in group_obj:
    print(key,list(value))

from itertools import count,cycle,repeat

# a = [1,2,3]

# for i in cycle(a):
#     print(i)





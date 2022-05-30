# lambda is a single line functions

add10 = lambda x: x+10 # now this is a function which returns by adding 10 to the input

print(add10(5))

mul = lambda x,y: x*y

print(mul(2,7))

point2D = [(2,4),(2.4,5),(-1,5)]
print2D_sorted = sorted(point2D) # This will be sorted based on the x value of the points by default

print(print2D_sorted)


# map function transforms each element with a function map(func,seq)

a=[1,2,3,4,5]

out = map(lambda  x: x*2,a)

print(list(out))

#another way

c = [x*2 for x in a]
print(c)

# filter(func,seq)

filt = filter(lambda x: x%2==0, a)

print(list(filt))

c = [x for x in a if x%2 == 0]

print(c)

#reduce(func,seq)

from functools import reduce

proda = reduce(lambda x,y: x*y , a)
print(proda)
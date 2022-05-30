# tuple is similar to list with immutable or unchangable properties

mytuple = tuple((1,2,3))

mylist_to_tuple = tuple([1,2,4,5])

print(mytuple,mylist_to_tuple)

print(mytuple[1],mytuple.count(1),mytuple[2:],mytuple.index(2))

dat = "Max","t",2,3,54

print(dat)

sam,text,w,e,r = dat

print(sam,text,w,e,r)

t1, *t2, t3 = dat

print(t1, t2, t3)

import sys

lst = [1,2,3]

tpl = (1,2,3)

print(sys.getsizeof(lst)," bytes")

print(sys.getsizeof(tpl)," bytes")
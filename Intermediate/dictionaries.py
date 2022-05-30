# dictinaries - key-value pair, Unordered, Mutable

from sqlalchemy import true


mydict = {"a":2,"b":"name","bol":True}

print(mydict)

newdict = dict(a=2,b="name",bol=True)

print(newdict)

if "b" in newdict:
    print(True)

newdict["sam"] = "bob"

del newdict["b"]

print(newdict)

mydict.pop("bol")

print(mydict)

mydict.popitem()

print(mydict)

for key,val in mydict.items():
    print(key,val)


numdict = {1:2,3:4,5:6}

tupdict = {(3,5):6}

numdict.update(tupdict)

print(numdict)

#collections : Counter, namedtuple, OrderedDict, defaultDict, deque

from collections import Counter,OrderedDict

#counter is used to store values counts as dictionaries

Sam_str = "jhgklkuygj"

mycounter = Counter(Sam_str)

print(mycounter , mycounter.keys(), mycounter.values(), mycounter.most_common(),mycounter.most_common(1))

from collections import namedtuple

Point = namedtuple('Point','x,y')
pt = Point(2,4)
print(pt.x,pt.y)

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['d'] = 3
ordered_dict['c'] = 4
print(ordered_dict)

from collections import defaultdict

# normal dict with default type mentioned so that if we access key that doesnt exist it will 
# give default value of type we specify

def_dict = defaultdict(int)
def_dict['a'] = 1
def_dict['b'] = 1
print(def_dict['a'],def_dict['c'])

from collections import deque

de = deque()

de.append(1)
de.append(2)

print(de)

de.appendleft(3)
de.pop()
print(de)

de.append(10)
de.popleft()
print(de)

de.extendleft([1,2,4,5])
de.rotate(2) #it rotates all elements in the array to two positions right
print(de)
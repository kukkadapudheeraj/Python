
from pymysql import MySQLError


my_list = [ "sample list" , 2 , 3.5, {"a":5},(4.6,7,8) , True]

print(my_list ,my_list[1],my_list[-2],my_list[2:3],my_list[2:],my_list[:3])

if  2 in my_list:
    print(True)
else:
    print(False)

print(len(my_list))

my_list.append(10)

my_list.insert(2,"inserted item")

print(my_list)

# remove or pop is used to remove in list

my_list.reverse()

print(my_list)


my_new_list = [0] * 10

print(my_new_list)

print(my_list[::2]) # this means to print beginning to end of array with incrementer of 2

my_list_copy = my_list

my_list_copy.append(100)

print(my_list)

my_list_copy = my_list.copy()

my_list_copy.pop()

print(my_list,"\n",my_list_copy)

list_def = list(my_list)

# list comprehension

i = [1,2,3,4,1,5,6,7,8,9]

j = [num*num for num in i]

print(j)




from audioop import avg
from random import sample
from statistics import mean
from math import *

from numpy import average

stri_name = "dheeraj"

print("My name is "+stri_name+" \n")

age = 22

print("My age is %d years old " %(age) )

is_male = True

print("My gender is male %s " %(is_male))

print("space to new line \nspace to tab \t and print this")

print("use double quotes inside print \" ")

print("concatenation this to my name as " + stri_name)

print("uppercase of my name is "+ stri_name.upper() )

print("lowercase of my name is "+ stri_name.lower())

print("check case %s" %(stri_name.isupper()))

print("check length of string like %d" %(len(stri_name)))

print("find index of start of character or sub string in string like %d" %(stri_name.index("j")))

print("replace character or substring in a string as "+stri_name.replace("d","D"))

print(0,1,2,3,4,12.34,-1,32,"1",True,1+2+3,2*4,1+(3*6%4))

print(str(age),int(age),float(age),bool(age),abs(age),pow(2,2),max(2,7),min(4,69))

print(floor(12.4567),ceil(12.345543),sqrt(144))

# Get input from user

# user_input = input("please enter a number or name : ")

# user_age = input("please enter a age : ")

# print(user_input + " has age of " + str(user_age) )

# Lists

sample_list = [age,stri_name,2,3,5.5]

print(sample_list , sample_list[2] ,sample_list[1:3],sample_list[2:],sample_list[:3])

another_list = ["12","12",4,5,7,7]

sample_list.extend(another_list)

print(sample_list)

sample_list.append(["1",3,52])

index = 4

sample_list.insert(4,"fourth_index_value")

print(sample_list)

sample_list.remove(3)

print(sample_list)

sample_list.pop()

print(sample_list)

print(sample_list.index(4))

print(sample_list.count(7))

sort_list = [3,42,245,-4,-5.6,82]

sort_list.sort()

print(sort_list)

new_list = another_list.copy()

print(new_list)

# tuples - Immutable( Un editable)

coords = (4,5)

print(coords[1:])

# coords[1] = 6 error because its immutable

#functions

def main(name):

    print("my name is "+ name)

    return name

name = main(name="dheeraj")

print(name)

if 0:
    print("false")
elif 1&0:
    print("True")
else:
    print("comes here")

if 0 or 1:
    print("True")

if 0 and 1:
    print("False")
else:
    print("comes here")

# Dictionaries - key,value pair

months = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March"
}

print(months["Jan"],months.get("Feb"),months.get("Dec","Not a valid key"),months.get("Dec",months.get("Mar")))


# while loop

i =1

while i!=0:
    print("yes")
    i=0

# for loop

arr = [1,2,3,4,"ert",1234.23]

for j in range(0,len(arr)):
    print(arr[j])

for let in "Dheeraj":
    print(let)

for let in arr:
    print(let)

for j in range(10,0,-2):
    print(j)

print(2**4) # exponent as 2 power 4

twod_arr = [[1,3],[3,5],[5,7]]

print(twod_arr[2][1])

'''
print("Multi line comment or doc string comments")
'''
# single line comment


# try:
#     num = int(input("Enter a valid integer"))
#     print(num)
# except:
#     print("Invalid input")

# files  w,r,a+,

file = open("sample.txt","r")
# file.write("THis is new file")
print(file.readlines())
file.close()

# modules
# REF : https://docs.python.org/3/py-modindex.html
import random

def print_rand():

    print(random.randint(0,100))

print_rand()




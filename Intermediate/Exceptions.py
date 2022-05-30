#Error and Exceptions

#syntax errors

# a  = 5 print(a) # syntax error

# a = 5 + '10' #  typecast error

# import somei # import error

# a = 5
# b = c # name error undefined

# f = open('s.txt') # file not found error

x = -5

# if x<0:
#     raise Exception('X value should be greater than 0')

# anotherway assert statement

# assert(x>=0), ' x is not positive'

try:
    a = 5/0
except Exception as e:
    print(e)







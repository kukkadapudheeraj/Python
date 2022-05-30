from pandas import concat


sam_text  = " my string \'iam a programmer\'"

print(sam_text)

new = "Hello \
    world"

print(new,new[2:3],new[2:],new[:-1],new[::-1])

t2 = "1sdvdssdf"

concat_text = new+t2

print(concat_text)

spc_str = "  spaced  string"

trm_str = spc_str.strip()

print(trm_str,trm_str.upper(),trm_str.lower(),trm_str.startswith(' '))

list_str = spc_str.split(' ')

print(list_str)

#string formatting using %,.format,f-string

num = 2
dec = 10.0
temp_str = "The value of num is %s and decimal is %f can be formated as %.2f"%(num,dec,dec)

print(temp_str)

temp_str = "The value of num is {} and decimal is {:f} can be formated as {:.2f}".format(num,dec,dec)

print(temp_str)

temp_str = f"The value of num is {num} and decimal is {dec} can be formated as {dec}"

print(temp_str)



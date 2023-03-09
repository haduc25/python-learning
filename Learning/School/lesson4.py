#### Function ####

# global (use when want to change value outside func from inside a func...) - https://www.w3schools.com/python/python_variables_global.asp
x = 10


def increment():
    global x
    x = 2
    x = x + 1
    print('x inside: ', x)


print('x outside[0]: ', x)
increment()
print('x outside[1]: ', x)


str1 = """Meow

    Meow
"""

str2 = '   haminhduc'
print(str1)
print(str2.upper())
print(str2.lower())
print(str2.strip())

# margin
str3 = 'haminhduc'
print(str3.rjust(30, '*'))
print(str3.ljust(30, '*'))
print(str3.center(30, '*'))

# length
print(str3.__len__())
print(len(str3))

print('='*30)
str4 = '  Ha Minh Duc'
print(str4.__len__())

str4 = str4.strip()
print(str4.__len__())

# startswith(), endswith(), find(), rfind(), lfind()
str5 = 'Meow'
print(str5.startswith('M'))
print(str5.startswith('Me'))
print(str5.endswith('w'))

print(str5.find('e'))  # -1/false, 0, 1/location first time founds


# count, split
print('='*30)

str = 'ha minh    duc'
str2 = str.split()

for i in str2:
    print(i, end=' - ')

# remove space
for i in range(len(str2)):
    str2[i] = str2[i].strip()

#
for i in range(len(str2)):
    print(str3)


##################
print('='*30)
str = 'ha minh duc'
print(str[2:])
print(str[:3])
print(str[:-2])
print(str[-2:])
print(str[2:-2])


##################
print('='*30)
str = 'ha minh duc'
start = 0
end = str.__len__()

print(str[start:end])
print(str[:end])
print(str[start:])

# join()
str = 'uid025;hà minh đức;1/1/2001'
arr = str.split(
)
print(arr)

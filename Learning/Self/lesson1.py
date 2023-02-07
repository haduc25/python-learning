# 1. String

print('#1. String')

#isalnum() - check str is text or numeric
print('\n====================> isalnum() <====================')
txt = 'minhduc123'
str = txt.isalnum()

print(str) #true

#isupper() - check str is uppercase
print('\n====================> isupper() <====================')

str = 'MEOW'.isupper() #true
print(str)

#isalpha() - check str is letter (a-z) alphabet
print('\n====================> isalpha() <====================')

str = 'MEOWmeowMeowmeoW'.isalpha() #true
print(str)

#isdecimal() - check str is decimals (0-9)
print('\n====================> isdecimal() <====================')

str = '2509'.isdecimal() #true
str2 = "\u0033".isdecimal() #unicode for 3
str3 = "\u0047".isdecimal() #unicode for G

print(str)
print({})


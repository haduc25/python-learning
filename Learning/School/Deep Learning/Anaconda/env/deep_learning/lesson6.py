# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 10:16:09 2023

@author: Admin
"""

"""
    Example about yield 
"""


## exam 1
# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         print('num: ', num)
#         num += 1

# gen = infinite_sequence()
# for i in range(10):
#     print(next(gen))


## exam 2
# def even_numbers_up_to(n):
#     i = 0
#     while i <= n:
#         if i % 2 == 0:
#             yield i
#         i += 1


# gen = even_numbers_up_to(10)
# for num in gen:
#     if num == 2:
#        next(gen)
#     if num == 6:
#         break
#     print(num)

## exam 3
# def my_generator():
#     yield 1
#     yield 2
#     yield 3

# gen = my_generator()
# print(next(gen)) # prints 1
# print(next(gen)) # prints 2
# print(next(gen)) # prints 3


## exam 4
# def my_generator():
#     yield 1
#     yield 2
#     yield 3

# gen = my_generator()

## create a reversed generator
# rev_gen = reversed(list(my_generator()))

# print(next(rev_gen)) # prints 3
# print(next(rev_gen)) # prints 2
# print(next(rev_gen)) # prints 1


## exam 5
# def generate_numbers():
#     yield 1
#     yield 5
#     yield 9
 
# for item in generate_numbers():
#     print(item)


########## Tham Khảo ##########
#https://cafedev.vn/tu-hoc-python-khi-nao-nen-su-dung-cau-lenh-yield-thay-vi-cau-lenh-return-trong-python/#:~:text=C%C3%A2u%20l%E1%BB%87nh%20yield%20th%C6%B0%E1%BB%9Dng%20%C4%91%C6%B0%E1%BB%A3c,kh%C3%B3a%20yield%20thay%20v%C3%AC%20return.





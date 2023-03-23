# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 18:29:06 2023

@author: Admin

Souce code from: https://www.geeksforgeeks.org/python-os-path-splitext-method/
"""
# Python program to explain os.path.splitext() method
	
# importing os module
import os

# path
path = '/home/User/Desktop/file.txt'

print('CURRENT PATH: ', path)

# Split the path in
# root and ext pair
root_ext = os.path.splitext(path)

# print root and ext
# of the specified path
print("ROOT: root part of '% s':" % path, root_ext[0])
print("EXT: ext part of '% s':" % path, root_ext[1], "\n")


# path
path = '/home/User/Desktop/'

# Split the path in
# root and ext pair
root_ext = os.path.splitext(path)

# print root and ext
# of the specified path
print("root part of '% s':" % path, root_ext[0])
print("ext part of '% s':" % path, root_ext[1])


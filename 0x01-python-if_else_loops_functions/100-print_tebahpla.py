#!/usr/bin/python3


'''
a = 97 z = 122
A = 65 Z = 90
'''

for x in range(122, 96, -1):
    if x % 2 != 0:
        char = x - 32
    else:
        char = x

    print("{:c}".format(char), end="")

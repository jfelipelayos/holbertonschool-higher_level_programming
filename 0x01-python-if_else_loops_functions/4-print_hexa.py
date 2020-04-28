#!/usr/bin/python3
num = 0

while num <= 98:
    hex_num = hex(num)
    print("{:d} = {:s}".format(num, hex_num))
    num += 1

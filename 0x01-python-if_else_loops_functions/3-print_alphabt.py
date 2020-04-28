#!/usr/bin/python3
x = 97

while x <= 122:

    if x == 101 or x == 113:
        x += 1

    print(chr(x), end="")

    if x == 122:
        print("\n")
    x += 1

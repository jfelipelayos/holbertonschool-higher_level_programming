#!/usr/bin/python3
def uppercase(str):
    for i in str:
        char = ord(i)
        if ord(i) >= 97 and ord(i) <= 122:
            char -= 32
        print("{:c}".format(char), end="")
    print("")

#!/usr/bin/python3
for dec in range(0, 9):
    for un in range(dec + 1, 10):
        if dec != 8:
            print("{:d}{:d}".format(dec, un), end=", ")
        else:
            print("{:d}{:d}".format(dec, un))

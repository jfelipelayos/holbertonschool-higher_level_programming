#!/usr/bin/python3
from sys import argv as av

if __name__ == "__main__":

    length = len(av) - 1

    if length == 0:
        print("{} arguments.".format(length))
    else:
        if length == 1:
            print("{:d} argument:".format(length))
            print("{:d}: {:s}".format(length, av[1]))
        else:
            print("{:d} arguments:".format(length))

            num = 0
            for i in av:
                if num != 0:
                    print("{:d}: {:s}".format(num, i))
                num = num + 1

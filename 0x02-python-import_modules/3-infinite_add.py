#!/usr/bin/python3
from sys import argv as numbers

if __name__ == "__main__":

    result = 0

    for i in range(1, len(numbers)):
        result += int(numbers[i])

    print(result)

#!/usr/bin/env python3
#username: rbhandari17@myseneca.ca
import sys
if len(sys.argv) != 3:
    print("Usage: ./lab2c.py <name> <age>")
    sys.exit()

name = sys.argv[1]
age = sys.argv[2]

print('Hi ' + name + ', you are ' + age + ' years old.')

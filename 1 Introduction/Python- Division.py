if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(int(a/b))
    print(float(a/b))
"""
Editorial by DOSHI
In Python 2, __future__ module includes a new type of division called integer division given by the operator //



Now / performs float division and // performs integer division.

Tested by DOSHI
Problem Tester's code:

Python 2

from __future__ import division
a = int(raw_input())
b = int(raw_input())

print a // b
print a / b
Python 3

a = int(input())
b = int(input())

print(a // b)
print(a / b)
"""

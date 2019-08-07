#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if((n%2==1) or ( n%2 == 0 and n >= 6 and n <= 20 )):
        print("Weird")
    elif((n>=2 and n <= 5) or (n>20) ):
        print("Not Weird")
"""
Set by shashank21j
Problem Setter's code:

Python 2

n = int(raw_input())
if n % 2 == 1:
    print "Weird"
elif n % 2 == 0 and 2 <= n <= 5:
    print "Not Weird"
elif n % 2 == 0 and 6 <= n <= 20:
    print "Weird"
else:
    print "Not Weird"
Python 3

n = int(input())
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
"""

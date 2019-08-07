if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print (i+1, end='')
"""
Editorial by DOSHI
Using the map() and the print _function, we can solve this in one line.

Set by shashank21j
Problem Setter's code:

Python 2

from __future__ import print_function
print(*range(1, input() + 1), sep="")  
Python 3

print(*range(1, int(input()) + 1), sep="")  
Tested by DOSHI
Problem Tester's code:

Python 2

from __future__ import print_function
map(lambda x: print(x + 1,end=''), range(input()))
Python 3

list(map(lambda x:print(x + 1, end=''), range(int(input()))))
"""

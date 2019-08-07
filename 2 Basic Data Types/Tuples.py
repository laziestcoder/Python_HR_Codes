#import '__builtins__'
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    l = []
    for i in integer_list:
        l.append(i)
    t = tuple(l)
    print(hash(t))

"""
Editorial by DOSHI
hash() is one of the functions in __builtins__ module, so we just need to create a tuple of the  elements and then pass it to the  function.

Tested by DOSHI
Problem Tester's code:

n = raw_input()
print hash(tuple([int(i) for i in raw_input().split()]))
"""

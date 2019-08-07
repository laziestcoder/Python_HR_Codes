if __name__ == '__main__':
    n = int(input())
    l = []
    for _ in range(n):
        s = input().split()
        if(s[0]=='insert'):
            a = int(s[1])
            b = int(s[2])
            l.insert(a, b)
        elif(s[0]=='print'):
            print(l)
        elif(s[0]=='remove'):
            a = int(s[1])
            l.remove(a)
        elif(s[0]=='append'):
            a = int(s[1])
            l.append(a)
        elif(s[0]=='sort'):
            l.sort()
        elif(s[0]=='pop'):
            l.pop()
        elif(s[0]=='reverse'):
            l.reverse()

"""
Editorial by DOSHI
We can solve this using list methods and conditionals.

Tested by DOSHI
Problem Tester's code:

arr = []
for i in range(int(raw_input())):
    s = raw_input().split()
    for i in range(1,len(s)):
        s[i] = int(s[i])
        
    if s[0] == "append":
        arr.append(s[1])
    elif s[0] == "extend":    
        arr.extend(s[1:])
    elif s[0] == "insert":
        arr.insert(s[1],s[2])
    elif s[0] == "remove":
        arr.remove(s[1])
    elif s[0] == "pop":
        arr.pop()
    elif s[0] == "index":
        print arr.index(s[1])
    elif s[0] == "count":
        print arr.count(s[1])
    elif s[0] == "sort":
        arr.sort()
    elif s[0] == "reverse":
        arr.reverse()
    elif s[0] == "print":
        print arr
"""

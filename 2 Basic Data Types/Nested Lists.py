if __name__ == '__main__':
    def sortSecond(val): 
        return val[1]  
    a = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append([name,score])
    #print(a)
    if(len(a)>1):
        a.sort(key = sortSecond)
    #print(a)
    lowest = a[0][1]
    #print("lowest")
    #print (lowest)
    ans = []
    for i in a:
        if(i[1]>lowest):
            ans.append(i)
    
    ans.sort(key = sortSecond)
    low = ans[0][1]
    #print("low")
    #print(low)
    #print("ans")
    #print (ans)
    a.clear()
    for i in ans:
        if(i[1]==low):
           # print(i)
            a.append(i[0])
    
    a.sort()
    #print("a")
    #print(a)
    for i in a:
        print (i)
"""
Editorial by DOSHI
We can solve this challenge by using nested list.

Problem Setter's code:

from __future__ import print_function
score_list = {}
for _ in range(input()):
    name = raw_input()
    score = float(raw_input())
    if score in score_list:
        score_list[score].append(name)
    else:
        score_list[score] = [name]
new_list = []
for i in score_list:
    new_list.append([i, score_list[i]])
new_list.sort()
result = new_list[1][1]
result.sort()
print (*result, sep = "\n")
Tested by DOSHI
Problem Tester's code:

a = [[raw_input(), float(raw_input())] for i in xrange(int(raw_input()))]
s = sorted(set([x[1] for x in a]))
for name in sorted(x[0] for x in a if x[1] == s[1]):
    print name
"""

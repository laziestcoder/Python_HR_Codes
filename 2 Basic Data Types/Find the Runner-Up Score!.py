if __name__ == '__main__':
    n = int(input())
    arr = list( map(int, input().split()))
    arr.sort(reverse=True)
    for i in arr:
        if(i<arr[0]):
            print(i)
            break

"""
Editorial by shashank21j
There are many ways to solve this problem.

This can be solved by maintaining two variables  and . Iterate through the list and find the maximum and store it. Iterate again and find the next maximum value by having an if condition that checks if it's not equal to first maximum.

Create a counter from the given array. Extract the keys, sort them and print the second last element.

Transform the list to a set and then list again, removing all the duplicates. Then sort the list and print the second last element.

Set by harsh_beria93
Problem Setter's code:

Python 2

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    m1 = max(arr)
    m2 = -9999999999
    for i in range(n):
        if arr[i] != m1 and arr[i] > m2:
            m2 = arr[i]
    print m2
from collections import Counter
if __name__ == '__main__':
    n = int(raw_input())
    arr = Counter(map(int, raw_input().split())).keys()
    arr.sort()
    print arr[-2]
from collections import Counter
if __name__ == '__main__':
    n = int(raw_input())
    arr = list(set(map(int, raw_input().split())))
    arr.sort()
    print arr[-2]
"""

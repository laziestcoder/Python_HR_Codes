def is_leap(year):
    leap = False
    
    # Write your logic here
    if((year%400 == 0) or ( year%4 == 0 and year%100 != 0)):
        leap= True
    
    return leap

"""
Editorial by shashank21j
Just implement a function using def and if-else logic.

Solutions
Python 2

def is_leap(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False

print is_leap(input())
Python 3

def is_leap(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False

print(is_leap(int(input())))
Python 2

def is_leap(year):
    return (year % 400 == 0) or (( year % 100 != 0) and (year % 4 == 0))
    
print is_leap(input())
"""

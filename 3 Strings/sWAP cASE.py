def swap_case(s):
    S = ""
    for i in s:
        S= S+"".join([i.upper() if i.islower() else i.lower()])
    return S

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

"""
Editorial by DOSHI
Use the method string.swapcase(s) to swap lower case letters to upper case letters and vice versa.


To learn more, visit:
https://docs.python.org/2/library/string.html#string.swapcase

Set by DOSHI
Problem Setter's code:

import string
print string.swapcase(raw_input())
"""

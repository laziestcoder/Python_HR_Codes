if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    a = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if(i+j+k != n ):
                    a.append([i,j,k])

    print(a)

"""
Editorial by DOSHI
List comprehensions are an elegant way where lists can be built without having to use different for loops to append values one by one.

Solution

Python 2
a, b, c, n = [int(raw_input()) for _ in xrange(4)]
print [[x,y,z] for x in xrange(a + 1) for y in xrange(b + 1) for z in xrange(c + 1) if x + y + z != n]
"""

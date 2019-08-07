if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    #print (student_marks[query_name][1])
    result = float(0)
    result = result + student_marks[query_name][0]
    result = result + student_marks[query_name][1]
    result = result + student_marks[query_name][2]
    result = float(result/3.00)
    print("{0:.2f}".format(result))

"""
Editorial by DOSHI
Use a dictionary to store the averages as values and the name as keys.

Tested by DOSHI
Problem Tester's code:

d={}
for i in range(int(raw_input())):
	line=raw_input().split()
	d[line[0]]=sum(map(float,line[1:]))/3

print '%.2f' % d[raw_input()]
"""

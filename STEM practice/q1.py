import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\CP\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\CP\\output.txt","w")

"""
Input:

1 0 0 7 0 0 0 0 0
0 3 2 0 0 0 0 0 0
0 0 0 6 0 0 0 0 0
0 8 0 0 0 2 0 7 0
5 0 7 0 0 1 0 0 0
0 0 0 0 0 3 6 1 0
7 0 0 0 0 0 2 0 9
0 0 0 0 5 0 0 0 0
3 0 0 0 0 4 0 0 5

Output:
[6, 18, 15, 13, 0, 0, 0, 0, 0]
[13, 19, 8, 8, 2, 9, 7, 7, 0]
[20, 21, 13, 9, 3, 10, 7, 7, 0]
[20, 15, 7, 6, 12, 20, 14, 8, 0]
[19, 7, 7, 4, 12, 13, 18, 10, 9]
[7, 0, 5, 8, 16, 12, 18, 10, 9]
[10, 0, 5, 9, 11, 6, 16, 14, 14]
[3, 0, 5, 9, 9, 4, 5, 5, 5]
[3, 0, 0, 4, 4, 4, 5, 5, 5]
"""
#-----------------------------------------------------
matrix = []
 
#input dimen
row = 9
col = 9

#sum mat dimen
sr = 3
sc = 3

for _ in range(row):
    matrix.append([int(x) for x in input().split()])

res = [[0 for x in range(col)] for x in range(row)]

def ifexists(m,n):
    if (0<=m and m<row and 0<=n and n<col):
        return matrix[m][n]
    else:
        return 0

for i in range(row):
    for j in range(col):
        for x in range(sr):
            for y in range(sc):
                temp = ifexists(i+x,j+y)
                res[i][j] += temp

for _ in res:
    print(_)

"""
for _ in range(row):
    matrix.append([int(x) for x in input().split()])

#res = [[0 for x in range(col)] for x in range(row)]

def ifexists(m,n):
    if (0<=m and m<row and 0<=n and n<col):
        return matrix[m][n]
    else:
        return 0

for i in range(row):
    for j in range(col):
        #_1 = ifexists(i,j)
        _2 = ifexists(i+1,j)
        _3 = ifexists(i+2,j)

        _4 = ifexists(i,j+1)
        _5 = ifexists(i+1,j+1)
        _6 = ifexists(i+2,j+1)

        _7 = ifexists(i,j+2)
        _8 = ifexists(i+1,j+2)
        _9 = ifexists(i+2,j+2)

        matrix[i][j] += _2+_3+_4+_5+_6+_7+_8+_9
        #res[i][j] +=  _1+_2+_3+_4+_5+_6+_7+_8+_9

for _ in matrix:
    print(_)
"""

"""
for _ in matrix:
    print(_)

print("---------------------------- \n")
for _ in res:
    print(_)
"""
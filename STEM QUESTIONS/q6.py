import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\CP\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\CP\\output.txt","w")

n = 5
matrix=[[1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]]
ans = []

def diag(matrix):
    for i in range(1,(n+n)):
        stc = max(0,i-n)
        c = min(i,(n-stc), n)
        for j in range(0,c):
            ans.append(matrix[min(n,i)-j-1][stc+j])

diag(matrix)
print(ans[::-1])
"""
for i in range(n):
    for j in range(n):
        ans.append(matrix[i][j])
"""
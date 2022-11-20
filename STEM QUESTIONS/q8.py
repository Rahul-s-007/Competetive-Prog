import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\CP\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\CP\\output.txt","w")

area = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
hd = [1,2,25,30,19,5,80,70,65,28,42,39,12,55,13,45,22]
vd = [2,2,1,1,5,6,4,2,3,3,2,4,1,2,1]

lst = [[1, 1, 2], [2, 2, 2], [3, 25, 1], [4, 30, 1], [5, 19, 5], [6, 5, 6], [7, 80, 4], [8, 70, 2], [9, 65, 3], [10, 28, 3], [11, 42, 2], [12, 39, 4], [13, 12, 1], [14, 55, 2], [15, 13, 1]]
ans = []


"""
for i in range(15):
    ans.append([area[i],hd[i],vd[i]])
"""
print(ans)

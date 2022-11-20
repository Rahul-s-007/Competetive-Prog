import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")

for temp in range(int(input())):
    l = int(input())
    arr = [int(x) for x in input().split()]
    s_arr = list(set(arr))
    flag = 0
    for i in s_arr:
        cnt = 0
        for j in arr:
            if(i == j):
                cnt += 1
        if(cnt > 2):
            flag = 1
            print("No")
            break
    if(flag == 0):
        print("Yes")
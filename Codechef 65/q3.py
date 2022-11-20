import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")

for temp in range(int(input())):
    n,k = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    if(k not in arr):
        print("No")
    else:
        flag = 0
        if(n==1):
            if(arr[0] == k):
                flag = 1
        else:
            for i in range(n-1):
                if(arr[i] == k):
                    flag = 1
                    break
        if(flag == 0):
            print("No")
        else:
            print("Yes")
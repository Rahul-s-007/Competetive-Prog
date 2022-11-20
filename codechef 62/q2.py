import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\CP\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\CP\\output.txt","w")

for temp in range(int(input())):
    n,x,y = [int(x) for x in input().split()]
    if(y%x==0):
        if(y/x <= n):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
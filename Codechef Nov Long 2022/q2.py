import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\CP\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\CP\\output.txt","w")

for temp in range(int(input())):
    l = int(input())
    arr = [int(x) for x in input().split()]
    ob = sum(arr)
    r = 2
    dnom = ob-r
    def permu(n):
        if (n == dnom):
            return 1
        else:
            return n*permu(n-1)
    print(permu(ob)%998244353)

import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")

for temp in range(int(input())):
    n,q = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    s = sum(a)
    #print(s)
    for i in range(q):
        l,r = [int(x) for x in input().split()]
        ele = r-l+1
        if(ele%2 == 1):
            s = s+1
    print(s)

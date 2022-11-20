import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")

#Start coding below
for temp in range(int(input())):
    n=int(input())
    perm = [int(x) for x in input().split()]
    k=0
    for ind,x in enumerate(perm):
        #print(ind,x)
        k=max(k,abs((ind+1)-x))
    print(k)

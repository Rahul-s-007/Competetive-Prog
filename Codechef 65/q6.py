import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")

for temp in range(int(input())):

    n,k = [int(x) for x in input().split()]
    if(n%k == 0):
        print(k)
        for j in range(n//k):
            for i in range(1,k+1):
                print(i,end=" ")
    else:
        for i in range(k,n+1):
            if(n%i >= k or n%i==0):
                k = i
                break
        rem = n%k
        print(k)
        for j in range(n//k):
            for i in range(1,k+1):
                print(i,end=" ")
        for i in range(1,rem+1):
            print(i,end=" ")
    print()
import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")

#"""
def kbits(n,k):
    for i in range(k):
        if(n>1):
            n = n//2
        else:
            n = 0
            break
    return n%2

for temp in range(int(input())):
    n,q = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    for _ in range(q):
        k, l1, r1, l2, r2 = [int(x) for x in input().split()]
        ans = 0
        for i in range(l1 , r1+1):
            for j in range(l2 , r2+1):
                a = arr[i-1]
                b = arr[j-1]
                res = kbits(a,k) ^ kbits(b,k)
                if(res == 1):
                    ans += 1
        print(ans)
#"""

"""
for temp in range(int(input())):
    n,q = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    for _ in range(q):
        ans = 0
        k, l1, r1, l2, r2 = [int(x) for x in input().split()]
        for i in range(l1 , r1+1):
            for j in range(l2 , r2+1):
                #print(i,j)
                #t1 = arr[i-1] ^ arr[j-1]
                s = bin(arr[i-1] ^ arr[j-1])[2:]
                if(len(s)>k):
                    if(s[-(k+1)] == "1"):
                        ans += 1
        print(ans)
"""
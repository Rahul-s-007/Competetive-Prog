import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")


for temp in range(int(input())):
    arr = [int(x) for x in input().split()]
    n = arr[0]
    k = arr[1]
    
    if(n==1):
        print(0)
    else:
        if(k >= n//2):
            print((n*(n-1))//2)
        else:
            ans = 0
            ans += ((n*(n-1))//2)-((n-k)*((n-k)-1)//2)
            ans += k*(n-(2*k))
            ans += (k*(k-1))//2
            print(ans)
"""
import math
for temp in range(int(input())):
    arr = [int(x) for x in input().split()]
    n = arr[0]
    k = arr[1]
    
    if(n==1):
        print(0)
    else:
        if(k >= n//2):
            print((n*(n-1))//2)
        else:
            ans = 0
            a = n-1
            d = -1
            ans += math.trunc( (k/2)*(2*a+((k-1)*d)) )
            ans += k*(n-(2*k))
            ans += (k*(k-1))//2
            print(ans)
"""

"""
import math
for temp in range(int(input())):
    arr = [int(x) for x in input().split()]
    n = arr[0]
    k = arr[1]
    
    if(n==1):
        print(0)
    else:
        if(k >= n//2):
            print(((n*(n+1))//2)-n)
        else:
            ans = 0
            t = k*2
            a = n-1
            d = -1
            ans = math.trunc( (t/2)*(2*a+((t-1)*d)) )
            print(ans)
"""
"""
import math
for temp in range(int(input())):
    arr = [int(x) for x in input().split()]
    n = arr[0]
    k = arr[1]
    
    if(n==1):
        print(0)
    else:
        if(k >= n//2):
            print(((n*(n+1))//2)-n)
        else:
            ans = 0
            t = k*2
            a = n-1
            d = -1
            ans = math.trunc( (t/2)*(2*a+((t-1)*d)) )
            #print(ans)
            print(ans)
"""
"""
import math
for temp in range(int(input())):
    arr = [int(x) for x in input().split()]
    n = arr[0]
    k = arr[1]
    
    if(n==1):
        print(0)
    else:
        if(k >= n//2):
            print(((n*(n+1))//2)-n)
        else:
            ans = 0
            a = n-1
            d = -1
            ans = math.trunc( (k/2)*(2*a+((k-1)*d)) )
            #print(ans)
            print((ans-k)*2)
"""
"""
for i in range(1,k+1):
    ans += n-i
"""
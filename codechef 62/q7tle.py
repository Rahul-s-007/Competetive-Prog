import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\CP\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\CP\\output.txt","w")

#import math
# Pathogarean Question 3rd last
for temp in range(int(input())):
    x = int(input())
    

"""
def is_sum(n):
    for j in range(int((n/2)**0.5), 1 + int((n-1)**0.5)):
        i2 = n - j * j
        i = int((i2)**0.5)
        if i * i == i2 and i > 0:
            print(i,j)
            return True
    return False

for temp in range(int(input())):
    x = int(input())
    if(is_sum(x)==False):
        print("-1")
"""

"""
def is_sum(n):
    rt = int((n)**0.5)
    if int(rt + 0.5) ** 2 == n:
        print("0",rt)
        return True
    else:
        for j in range(int((n/2)**0.5), 1 + int((n-1)**0.5)):
            i2 = n - j * j
            i = int((i2)**0.5)
            if i * i == i2 and i > 0:
                print(i,j)
                return True
        return False

for temp in range(int(input())):
    x = int(input())
    if(is_sum(x)==False):
        print("-1")
"""

"""
N = 100
from math import isqrt, gcd

for m in range(isqrt(N-1)+1):
    for n in range(1+m%2, min(m, isqrt(N-m*m)+1), 2):
        if gcd(m, n) > 1:
            continue
        a = m*m - n*n
        b = 2*m*n
        c = m*m + n*n

        for k in range(1, N//c+1):
            print(k*a, k*b, k*c)
"""

"""
for temp in range(int(input())):
    n = int(input())
    flag = 0
    #lim = int((n**0.5)/2)
    for i in range(n):
        for j in range(i,n):
            if((i*i + j*j) == n):
                print(i,j)
                flag = 1
                break
        if(flag==1):
            break
    if(flag==0):
        print("-1")
"""

"""
for temp in range(int(input())):
    n = int(input())
    c = 0
    for i in range(1,int(n**0.5)+1):
        square = i * i
        diff = n - square # Subtract the square from given N
        sqdif = int(diff**0.5) #  Check if the difference is also a perfect square
        if sqdif * sqdif == diff :
            c += 1
            print(i,sqdif) #print the pairs
            break
    if c==0:
        print("-1")
"""
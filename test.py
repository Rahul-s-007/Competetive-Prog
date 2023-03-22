"""
import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")
"""
# n = 3
# for i in range(1,n-1):
#     print(i)

"""
000
001
010
100
011
101
110
111
"""
# 001
# 011

"""
s = "aaa"
print(s.count("aa"))  # output 1
"""

"""
t1 = 1 ^ 2
t2 = format(t1 , 'b')
print(t2)
"""
"""
def kbits(n,k):
    for i in range(k):
        if(n>1):
            n = n//2
        else:
            n = 0
            break
    return n%2

print(kbits(5,5))
print(bin(5))
"""

"""
5 // 2 = 2
2 // 2 = 1
1 // 2 = 0
"""
"""
t1 = 1 ^ 2
t2 = format(t1 , 'b')
print(t2)
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
5 // 2 = 2
2 // 2 = 1
1 // 2 = 0
"""
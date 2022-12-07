import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")


# list1, list2 = (list(t) for t in zip(*sorted(zip(list1, list2))))
#res, a, b = (list(t) for t in zip(*sorted(zip(res, a, b))))

for temp in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    #print(a)
    #print(b)
    res = [b[i]/a[i] for i in range(n)]
    #print(res)
    res, a, b = (list(t) for t in zip(*sorted(zip(res, a, b))))
    #print(res)
    #print(a)
    s = 0
    ans = 0
    for i in range(1,n):
        s += a[i-1]
        ans += s * b[i]
    print(ans)
    #print("-----------")

"""
for temp in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    #res = [b[i]/a[i] for i in range(n)]
    res = []
    for i in range(n):
        res.append(b[i]/a[i])
    #print(res)
    for i in range(n):
        for j in range(i+1,n):
            if(res[i] > res[j]):
                temp = res[i]
                res[i] = res[j]
                res[j] = temp 
                
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
                
                temp = b[i]
                b[i] = b[j]
                b[j] = temp
                
    #print(res)
    #print(a)
    s = 0
    ans = 0
    for i in range(1,n):
        s += a[i-1]
        ans += s * b[i]
    print(ans)
    #print("-----------")
"""
"""
for temp in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    d = {}

    res = []
    for i in range(n):
        res.append(b[i]/a[i])
    #print(res)
    for i in range(n):
        for j in range(i+1,n):
            if(res[i] > res[j]):
                temp = res[i]
                res[i] = res[j]
                res[j] = temp 
                
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
                
                temp = b[i]
                b[i] = b[j]
                b[j] = temp
                
                
    #print(res)
    #print(a)
    
    d[a[0]] = 0
    s = 0
    ans = 0
    for i in range(1,n):
        s += a[i-1]
        d[a[i]] = s * b[i]
        ans += d[a[i]]
    
    print(ans)
    #print(d)
    #print("-----------")
"""


"""
for temp in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    d = {}

    res = []
    for i in range(n):
        res.append(b[i]/a[i])
    #print(res)
    for i in range(n):
        for j in range(i+1,n):
            if(res[i] > res[j]):
                temp = res[i]
                res[i] = res[j]
                res[j] = temp 
                
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
                
                temp = b[i]
                b[i] = b[j]
                b[j] = temp
                
                
    #print(res)
    #print(a)
    
    d[a[0]] = 0
    s = 0
    for i in range(1,n):
        s += a[i-1]
        d[a[i]] = s

    #print(d)
    
    ans = 0
    for i in range(n):
        ans += d[a[i]] * b[i]
    print(ans)
    #print("-----------")
"""
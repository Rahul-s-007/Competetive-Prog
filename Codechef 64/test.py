import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")

for temp in range(int(input())):
    l = int(input())
    s = [int(x) for x in input().split()]
    #t = s
    #cpy = t
    #ele = []
    def calc(tt):
        #print("-------------------")
        length = len(tt)
        #flag = 0
        #print(tt)
        for i in range(length):
            for j in range(i+1,length):
                if(tt[i] == tt[j]):
                    del tt[i:j]
                    #print(tt)
                    #flag = 1
                    return tt
        return tt

    for i in range(l):
        if(len(s)>1):
            s = calc(s)
        else:
            break

    """
    for i in range(l):
        try:
            if(len(s)>1):
                s = calc(s)
            else:
                break
        except:
            pass
    """
    ans = len(s)
    #print(ans)
    if(ans<=2):
        print("YES")
    else:
        print("NO")

"""
for temp in range(int(input())):
    a,b = [int(x) for x in input().split()]
    fac = []
    def distinctPrimeFactors(N):
        if (N < 2):
            #print(-1)
            fac.append(N)
            return
        if N == 2:
            #print(2)
            fac.append(2)
            return
        visited = {}
        i = 2
        while(i * i <= N):
            while(N % i == 0):
                if(i not in visited):
                    fac.append(i)
                    #print(i , end = " ")
                    visited[i] = 1
                N //= i
            i+=1
        if(N > 2):
            #print(N)
            fac.append(N)
    distinctPrimeFactors(b)
    flag = 0
    for i in fac:
        if(a%i != 0):
            print("NO")
            flag = 1 
            break
    if(flag == 0):
        print("YES")
"""

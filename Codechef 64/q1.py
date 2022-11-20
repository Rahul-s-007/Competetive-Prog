import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\CP\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\CP\\output.txt","w")

#t = [int(x) for x in input().split()]
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
    #print(fac)

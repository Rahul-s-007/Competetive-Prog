import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")

for temp in range(int(input())):
    n,k,l = [int(x) for x in input().split()]
    edges = 0
    
    if((k+l) == n):
        edges = k*l
    
    elif((k+l) < n):
        inter = n - (k+l)
        sc = k*(inter + l)
        
        it = (inter*(inter-1))//2
        it += inter*l
        
        edges = sc + it
    
    else:
        scsk = (k+l) - n
        edges = (k-scsk) * (l-scsk)
    
    print(edges)

"""
for temp in range(int(input())):
    n,k,l = [int(x) for x in input().split()]
    edges = 0
    
    if(k+l == n):
        edges = k*l
    
    elif(k+l < n):
        inter = n - (k+l)
        sc = k*(inter + l)
        it = int(inter*(inter-1)/2) + (inter*l)
        edges = sc + it
        
        #for i in range(1,inter+1):
        #    it += (inter-i) + l
        #edges = sc + it
        #edges = (k*(inter + l)) + (inter*(l))
    else:
        scsk = (k+l) - n
        edges = (k-scsk) * (l-scsk)
    
    print(edges)
"""
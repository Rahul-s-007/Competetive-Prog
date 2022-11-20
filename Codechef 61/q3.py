import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\CP\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\CP\\output.txt","w")

for temp in range(int(input())):
    l = int(input())
    a = str(input())
    b = str(input())

    d={}
    for c in a:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    common = ""

    for c in b:
        if c in d and d[c] > 0:
            common += c
            d[c] -= 1

    uni_com=[]
    [uni_com.append(x) for x in common if x not in uni_com]
    max_freq=0
    
    for i in uni_com:
        sum=0
        for j in common:
            if(i==j):
                sum += 1
        max_freq = max(max_freq,sum)

    print(max_freq)

    """
    #Dynamic programming
    lcs = zeros = [ [0] * (l+1) for _ in range(l+1)]

    for i in range(l):
        for j in range(l):
            if(a[i]==b[j]):
                lcs[i+1][j+1] = 1+ lcs[i][j]
            else:
                lcs[i+1][j+1] = max(lcs[i][j+1],lcs[i+1][j])
    #print(lcs[l][l])
    x=lcs[l][l]
    for i in lcs:
        print(i)
    """
    """
    Recursion
    def lcs(i,j):
        if(i == l or j == l):
            return 0
        elif(a[i]==b[j]):
            return 1+ lcs(i+1,j+1)
        else:
            return max(lcs(i+1,j),lcs(i,j+1))
    ans = lcs(0,0)
    """
    """
    for i in lcs:
        print(i)
    """
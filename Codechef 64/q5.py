import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")

"""
for temp in range(int(input())):
    l = int(input())
    s = [int(x) for x in input().split()]
    ans = l
    for i in range(l):
        for j in range(i+1,l):
            if(s[i] == s[j]):
                t = i + l - (j+1)
                ans = min(ans , t)
    if(ans<=2):
        print("YES")
    else:
        print("NO")
"""

for temp in range(int(input())):
    l = int(input())
    s = [int(x) for x in input().split()]
    t = s
    #ans = l
    ele = []
    for i in range(l):
        for j in range(i+1,l):
            if(s[i] == s[j]):
                t = s[j::]
            #else:
            #    t = s[j::]
                #t = i + l - (j+1)
                #ans = min(ans , t)
    #print(t)
    ans = len(t)
    #"""
    if(ans<=2):
        print("YES")
    else:
        print("NO")
    #"""

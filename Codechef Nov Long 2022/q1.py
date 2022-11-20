import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")

for temp in range(int(input())):
    l = int(input())
    s = str(input())
    if(l%2==0):
        ans = ord(s[0])
        for i in range(1,l):
            ans = ans^ord(s[i])
        if(ans == 0):
            print("YES")
        else:
            print("NO")
        #pass
    else:
        print("NO")
"""
for temp in range(int(input())):
    l = int(input())
    s = str(input())
    uni = []
    for i in s:
        if i not in uni:
            uni.append(i)
    #print(len(uni) , l)
    uni_l = len(uni)
    if(l>uni_l):
        if(l % uni_l == 0):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
"""
"""
for temp in range(int(input())):
    l = int(input())
    s = str(input())
    s = list(s)
    #print(s)
    ans = ord(s[0])
    for i in range(1,l):
        ans = ans^ord(s[i])
    print(ans)
    if(ans == 0):
        print("YES")
    else:
        print("NO")
"""
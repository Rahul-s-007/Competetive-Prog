import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\CP\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\CP\\output.txt","w")

for temp in range(int(input())):
    l = int(input())
    s = [int(x) for x in input().split()]
    mini = min(s)
    ans = 0
    #"""
    for i in range(l):
        if(s[i] != mini):
            if(s[i]%mini == 0):
                ans += 1
            elif(ans == 0):
                ans+=1
                for j in range(i,l):
                    if(mini!=s[j]):
                        ans = ans + 1
                break
    #"""
    print(ans)
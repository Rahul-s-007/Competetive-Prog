import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")

for temp in range(int(input())):
    l = int(input())
    b = str(input())
    ans=0
    for i in range(0,l-1):
        if(b[i]==b[i+1]):
            ans=ans+1
    print(ans)
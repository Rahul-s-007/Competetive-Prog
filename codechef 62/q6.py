import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\CP\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\CP\\output.txt","w")

for temp in range(int(input())):
    length = int(input())
    s=list(str(input()))
    change = 0
    for i in range(1,length):
        if(s[i-1] != s[i]):
            if(s[i-1] == "1"):
                change += 1
    #ans = change-1 if change>1 else change
    print(change)

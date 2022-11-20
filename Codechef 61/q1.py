import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\CP\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\CP\\output.txt","w")

for temp in range(int(input())):
    t = [int(x) for x in input().split()]
    a=t[0]
    b=t[1]
    c=t[2]
    #print(a,b,c)
    if((a+b) % 2 == 1):
        print("Yes")
    elif((a+c) % 2 == 1):
        print("Yes")
    elif((b+c) % 2 == 1):
        print("Yes")
    else:
        print("NO")
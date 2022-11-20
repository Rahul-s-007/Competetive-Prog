import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")

for temp in range(int(input())):
    x,y = [int(x) for x in input().split()]
    if(y%x==0):
        print("YES")
    elif((2*x)<=y):
        print("YES")
    else:
        print("NO")

"""
for temp in range(int(input())):
    x,y = [int(x) for x in input().split()]
    if(y-x >= x):
        if((y%x) == 0):
            print("YES")
        else:
            flag = 0
            for i in range(1,y-x):
                n = y+i
                d = x+i
                if(n%d == 0):
                    print("YES")
                    flag = 1
                    break
            if(flag==0):
                print("NO")
    else:
        print("NO")
"""

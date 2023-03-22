import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")
import sys 
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")

for temp in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    
    a_one = a.count(1)
    b_one = b.count(1)
    flag = 0
    
    if(a == b):
        print("YES")
    elif(a[0] != b[0] or a[-1] != b[-1]):
        print("NO")
    else:
        if(a_one>b_one):
            print("NO")
        else:
            if(n == 3):
                if(a[1] == 0):
                    if(a[0]==1 or a[-1]==1):
                        print("YES")
                    else:
                        print("NO")
                else:
                    print("NO")

            else:
                for i in range(1,n-1):
                    if(a[i] == 1 and b[i]==0):
                        flag = 1
                        break
                    
                if(flag == 0):
                    if(a_one == 0):
                        if(b_one > 0):
                            print("NO")
                        else:
                            print("YES")
                    else:
                        print("YES")
                else:
                    print("NO")
                    

"""
for temp in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    
    a_one = a.count(1)
    b_one = b.count(1)
    
    if(n==3):
        if(a == b):
            print("YES")
        else:
            print("NO")

    else:
        if(a_one == 0):
            if(b_one > 0):
                print("NO")
            else:
                print("YES")
    
        elif(a_one > 0):
            if(b_one > 0):
                if(a_one < 2):
                    print("NO")
                else:
                    print("YES")
    
            elif(b_one == 0):
                if((n-a_one) < 2):
                    print("NO")
                else:
                    print("YES")
"""
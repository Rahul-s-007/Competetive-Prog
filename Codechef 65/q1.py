import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")

for temp in range(int(input())):
    a,b = [int(x) for x in input().split()]
    s = a+b
    flag = 0
    rt = int(s**0.5)
    #print(rt)
    for i in range(2,int(s**0.5)+1):
        if(s%i == 0):
            flag = 1
            print("Bob")
            break
    if(flag == 0):
        print("Alice")

"""
        if(n%2==0):
            m = n//2
        else:
            m = n//2 + 1
"""
"""
        if(arr[0] == k):
            print("Yes")
        elif(arr[int(n/2)] == k):
            print("Yes")
        else:
            print("No")
"""
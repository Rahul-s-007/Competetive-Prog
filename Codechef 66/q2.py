import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")

for temp in range(int(input())):
    arr = [int(x) for x in input().split()]
    n = arr[0]
    a = arr[1]
    b = arr[2]
    time = 0
    while(n>0):
        n = n//2
        if(n>0):
            time += a
            time += b
    print(time-b)
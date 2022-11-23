import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")

for temp in range(int(input())):
    arr = [int(x) for x in input().split()]
    if(arr[0] > arr[1]+arr[2]):
        print("YES")
    elif(arr[1] > arr[0]+arr[2]):
        print("YES")
    elif(arr[2] > arr[0]+arr[1]):
        print("YES")
    else:
        print("NO")
    
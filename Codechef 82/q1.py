# import sys 
# sys.stdin = open("input.txt","r")
# sys.stdout = open("output.txt","w")

for temp in range(int(input())):
    arr = [int(x) for x in input().split()]
    c = arr[1]/5
    if(c>arr[0]):
        print("NO")
    else:
        print("YES")

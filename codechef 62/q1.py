import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")

for temp in range(int(input())):
    t = [int(x) for x in input().split()]
    ans = max(t) - min(t)
    print(ans)
    
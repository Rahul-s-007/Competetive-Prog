import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\CP\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\CP\\output.txt","w")

for temp in range(int(input())):
    n,k,l = [int(x) for x in input().split()]
    edges = 0
import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\CP\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\CP\\output.txt","w")
"""
6
20
14
"""

def printSubsequences(arr, index, subarr):
    if index == len(arr):
        if len(subarr) != 0:
            check_condition(subarr)
            print(subarr , end=",")
    else:
        printSubsequences(arr, index + 1, subarr)
        printSubsequences(arr, index + 1, subarr+[arr[index]])
    return

def check_condition(lst):
    global ans
    s = sum(lst)
    if(s%k != 0):
        ans += 1
    return

for temp in range(int(input())):
    n,k = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    ans = 0
    printSubsequences(arr, 0, [])
    print(ans)
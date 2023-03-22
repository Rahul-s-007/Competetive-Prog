for temp in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    m = min(arr)
    c = arr.count(m)
    print(n-c)
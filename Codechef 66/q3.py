for temp in range(int(input())):
    arr = [int(x) for x in input().split()]
    n = arr[0]
    m = arr[1]
    k = arr[2]
    x = arr[3]
    
    pre_year = (k-1)*n
    mob_year = n+m
    k_total = pre_year + mob_year
     
    total = x % k_total
    
    if(total==0):
        print("YES")
    elif(total<=pre_year):
        print("NO")
    else:
        print("YES")

"""
for temp in range(int(input())):
    arr = [int(x) for x in input().split()]
    n = arr[0]
    m = arr[1]
    k = arr[2]
    x = arr[3]
    
    pre_year = (k-1)*n
    mob_year = n+m
    k_total = pre_year + mob_year
    total = 0
    
    while(total<x):
        total += k_total
        if(total>=x):
            if(x>(total-mob_year)):
                print("YES")
            else:
                print("NO")
"""


"""
for temp in range(int(input())):
    arr = [int(x) for x in input().split()]
    n = arr[0]
    m = arr[1]
    k = arr[2]
    x = arr[3]
    
    pre_year = (k-1)*n
    mob_year = n+m
    #k_total = pre_year + mob_year
    total = 0
    
    while(total<x):
        total += pre_year
        if(total>=x):
            print("NO")
            break
        else:
            total += mob_year
            if(total>=x):
                print("YES")
                break
"""
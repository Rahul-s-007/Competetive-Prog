import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")

"""
lst = ['a', 'b', 'c']
i = lst.index('b') # This raises ValueError if there's no 'b' in the list.
lst[i:i+1] = 'b1', 'b2', 'b3'

del a[-1] removes las element (by index)
"""

"""
1 2 3 4 5

1 2 3 4 5
"""
"""
even compre middle two and make equal then remove both
if only 2 elements left then replace small , big-small , small and end loop


odd compare each side and then replace the largest between then make qual of largest and middle then remove them
"""

"""
1 2 3 4 5 

1 2 3 3 1 5  -1

1 2 1 5

1 1 1 1 5   -2

1 1 5

1 1 1 4     -3

1 4

1 3 1       -4

--------

3 7 6 4

3 1 6 6 4   -1

3 1 4

3 1 1 3     -2

3 3

----------
"""

def n_even(l,lst):
    #print(lst)
    global cng
    hf = l//2
    m1 = hf - 1
    m2 = hf
    flag = 0
    
    if(l==2):
        e1 = lst[0]
        e2 = lst[1]
        if(e1 != e2):
            tmin = min(e1,e2)
            tmax = max(e1,e2)
            lst = [tmin,tmax-tmin,tmin]
            cng += 1
            flag = 1
            n_odd(l+1,lst)

    else:
        for i in range(hf-1):
            e1 = lst[m1-i]
            e2 = lst[m2+i]
            if(e1 != e2):
                if(e1>e2):
                    lst[m1-i] = e1-e2
                    del lst[m2+i]

                    cng += 1
                    flag = 1
                    n_odd(l-1,lst)
                
                else:
                    lst[m1-i] = e2-e1
                    del lst[m2+i]

                    cng += 1
                    flag = 1
                    n_odd(l-1,lst)

    if(flag == 0):
        print(cng)
        #return cng 

    
def n_odd(l,lst):
    #print(lst)
    global cng
    hf = (l-1)//2
    m = hf
    em = lst[hf]
    flag = 0

    if(l==3):
        e1 = lst[0]
        e2 = lst[2]

        if(e1 != e2):
                if(e2>e1):
                    if(em>e2):
                        lst[m] = em-e2
                        del lst[m+1]

                        cng += 1
                        flag = 1
                        n_even(l-1,lst)
                    else:
                        lst[m] = e2-em
                        del lst[m+1]

                        cng += 1
                        flag = 1
                        n_even(l-1,lst)
                
                else:
                    if(em>e1):
                        lst[m] = em-e1
                        del lst[m-1]

                        cng += 1
                        flag = 1
                        n_even(l-1,lst)
                    else:
                        lst[m] = e1-em
                        del lst[m-1]

                        cng += 1
                        flag = 1
                        n_even(l-1,lst)

    else:
        for i in range(1,hf):
            e1 = lst[m-i]
            e2 = lst[m+i]
            
            if(e1 != e2):
                if(e2>e1):
                    if(em>e2):
                        lst[m] = em-e2
                        del lst[m+i]

                        cng += 1
                        flag = 1
                        n_even(l-1,lst)
                    else:
                        lst[m] = e2-em
                        del lst[m+i]

                        cng += 1
                        flag = 1
                        n_even(l-1,lst)
                
                else:
                    if(em>e1):
                        lst[m] = em-e1
                        del lst[m-i]

                        cng += 1
                        flag = 1
                        n_even(l-1,lst)
                    else:
                        lst[m] = e1-em
                        del lst[m-i]

                        cng += 1
                        flag = 1
                        n_even(l-1,lst)

    if(flag == 0):
        print(cng)
        #return cng

for temp in range(int(input())):
    cng = 0

    n = int(input())
    arr = [int(x) for x in input().split()]

    if(n==1):
        print(0)
    else:
        if(n%2 == 0):
            n_even(n,arr)
        else:
            n_odd(n,arr)

    #print("-----------------")

"""
def n_even(l,lst):
    global cng
    m1 = (l/2)-1
    m2 = (l/2)

    flag = 0
    for i in range(l/2):
        e1 = lst[m1-i]
        e2 = lst[m2+i]
        if(e1 != e2):
            if(e1>e2):
                lst[(m1-i):(m1-i)+1] = e2-e1 , e1
                cng += 1
                flag = 1
                n_odd(l+1,lst)
            else:
                lst[(m2+i):(m2+i)+1] = e2 , e1-e2
                cng += 1
                flag = 1
                n_odd(l+1,lst)

    if(flag == 0):
        return cng 

    
def n_odd(l,lst):
    pass


for temp in range(int(input())):
    global cng
    cng = 0

    n = int(input())
    arr = [int(x) for x in input().split()]
    
    if(n%2 == 0):
"""
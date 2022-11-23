import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")
"""
Number of zeroes: 3 
Number of ones: 2
Number of 01: 1 
Number of 10: 2
----------------------------------
Number of zeroes: 0 
Number of ones: 5
Number of 01: 0 
Number of 10: 0
----------------------------------
"""

for temp in range(int(input())):
    s = str(input())
    l = len(s)
    zo_cnt = s.count("01")
    oz_cnt = s.count("10")
    ans = 0
    for i in range(1,l-1):
        zo = 0
        oz = 0
        if(s[i] == "0"):
            if(s[i+1] == "0"):
                oz += 1
            else:
                zo -= 1
            if(s[i-1] == "0"):
                zo += 1
            else:
                oz -= 1
        else:
            if(s[i+1] == "1"):
                zo += 1
            else:
                oz -= 1            
            if(s[i-1] == "1"):
                oz += 1
            else:
                zo -= 1

        if((oz_cnt+oz) == (zo_cnt+zo)):
            ans += 1
    
    zo = 0
    oz = 0
    if(s[0] == "0"):
        if(s[1] == "0"):
            oz += 1
        else:
            zo -= 1
    else:
        if(s[1] == "1"):
            zo += 1
        else:
            oz -= 1
    if((oz_cnt+oz) == (zo_cnt+zo)):
        ans += 1

    zo = 0
    oz = 0
    if(s[-1] == "0"):
        if(s[-2] == "1"):
            zo += 1
        else:
            oz -= 1
    else:
        if(s[-2] == "1"):
            oz += 1
        else:
            zo -= 1
    if((oz_cnt+oz) == (zo_cnt+zo)):
        ans += 1

    print(ans)

"""
for temp in range(int(input())):
    s = str(input())
    #print(s)
    l = len(s)

    zo_cnt = s.count("01")
    oz_cnt = s.count("10")
    print(zo_cnt,oz_cnt)
    ans = 0

    for i in range(1,l-1):
        #print(s[i])
        zo = 0
        oz = 0
        if(s[i] == "0"):
            if(s[i+1] == "0"):
                oz += 1
            elif(s[i+1] == "1"):
                zo -= 1
            if(s[i-1] == "0"):
                zo += 1
            elif(s[i-1] == "1"):
                oz -= 1
        else:
            if(s[i+1] == "1"):
                zo += 1
            elif(s[i+1] == "0"):
                oz -= 1            
            if(s[i-1] == "1"):
                oz += 1
            elif(s[i-1] == "0"):
                zo -= 1

        if((oz_cnt+oz) == (zo_cnt+zo)):
            #print(i+1)
            ans += 1
    
    zo = 0
    oz = 0
    if(s[0] == "0"):
        if(s[1] == "0"):
            oz += 1
        if(s[1] == "1"):
            zo -= 1
    else:
        if(s[1] == "1"):
            zo += 1
        elif(s[1] == "0"):
            oz -= 1
    if((oz_cnt+oz) == (zo_cnt+zo)):
        #print(i+1)
        ans += 1

    zo = 0
    oz = 0
    if(s[-1] == "0"):
        if(s[-2] == "1"):
            zo += 1
        if(s[-2] == "0"):
            oz -= 1
    else:
        if(s[-2] == "1"):
            oz += 1
        elif(s[-2] == "0"):
            zo -= 1
    if((oz_cnt+oz) == (zo_cnt+zo)):
        #print(i+1)
        ans += 1

    #print()
    print(ans)
    #print("---")
"""




"""
for temp in range(int(input())):
    s = str(input())
    
    z_cnt = s.count("0")
    o_cnt = s.count("1")

    zo_cnt = s.count("01")
    oz_cnt = s.count("10")
    
    re_zo = zo_cnt
    re_oz = oz_cnt

    ans = 0

    for i in range(1,len(s)-1):
        zo_cnt = re_zo
        oz_cnt = re_oz
        if(s[i] == "0"):
            if(s[i+1] == "0"):
                oz_cnt += 1
            if(s[i+1] == "1"):
                zo_cnt -= 1
            
            if(s[i-1] == "0"):
                zo_cnt += 1
            if(s[i-1] == "1"):
                oz_cnt -= 1
        else: # == 1
            if(s[i+1] == "1"):
                zo_cnt += 1
            if(s[i+1] == "0"):
                oz_cnt -= 1
            
            if(s[i-1] == "1"):
                oz_cnt += 1
            if(s[i-1] == "0"):
                zo_cnt -= 1

        if(oz_cnt == zo_cnt):
            ans += 1
    
    zo_cnt = re_zo
    oz_cnt = re_oz
    if(s[0] == "0"):
        if(s[1] == "0"):
            oz_cnt += 1
        if(s[1] == "1"):
            zo_cnt -= 1
        if(oz_cnt == zo_cnt):
            ans += 1
    
    zo_cnt = re_zo
    oz_cnt = re_oz
    if(s[-1] == "1"):
        if(s[-2] == "1"):
            zo_cnt += 1
        if(s[-2] == "0"):
            oz_cnt -= 1
        if(oz_cnt == zo_cnt):
            ans += 1

    print(ans)
"""

    #print("Number of zeroes:",z_cnt,"\nNumber of ones:",o_cnt)
    #print("Number of 01:",zo_cnt,"\nNumber of 10:",oz_cnt)
    #print("----------------------------------")
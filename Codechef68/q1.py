import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")

#Question: https://www.codechef.com/START68C/problems/BORSTR?tab=statement
#Sol: https://www.codechef.com/viewsolution/81985882 


"""
for temp in range(int(input())):
    l = int(input())
    s = str(input())

    set_l = len(set(s))
    max_sc = l - set_l
    ch = "abcdefghijklmnopqrstuvwxyz"

    if(set_l == 1):
        print(l-1)
    elif(l == set_l):
        print(0)
    else:
        flag = 0
        for j in reversed(range(1,max_sc+1)):
            for i in ch:
                if(s.count(i*j) >= 2):
                    print(j)
                    flag = 1
                    break
            if(flag == 1):
                break
"""


"""
for temp in range(int(input())):
    l = int(input())
    s = str(input())

    set_l = len(set(s))
    max_sc = l - set_l
    print(max_sc)
    
    ch = "abcdefghijklmnopqrstuvwxyz"
    
    flag = 0
    for j in reversed(range(1,max_sc+1)):
        for i in ch:
            if(s.count(i*j) >= 2):
                print(j)
                flag = 1
                break
        if(flag == 1):
            break

    if(flag==0):
        print(0)
    print("-----")
"""


"""
for temp in range(int(input())):
    l = int(input())
    s = str(input())

    s_set = set(s)
    set_l = len(s_set)
    print(len(set(s)))
    print(l)

    if(set_l == 1):
        print(l-1)
    elif(l == set_l):
        print(0)
    elif(l - set_l == 1):
        print(1)
    else:
        max_lim = l - set_l
        print(max_lim)
        #print(l-set_l)
    print("----------")
"""


"""
for temp in range(int(input())):
    l = int(input())
    s = str(input())

    ss = ""
    max_len = 0
    for i in range(l):
        #print(s[i])
        ss = ""
        fir = s[i]
        le = 1
        for j in range(i+1,l):
            if(fir == s[j]):
                ss += s[j]
                le += 1
                if(j == l-1):
                    if(ss in s[i+1:l]):
                        max_len = max(max_len, le)
            else:
                #print(ss)
                if(ss in s[i+1:l]):
                    max_len = max(max_len, le)
                break
    print(max_len)
    print("----------")
"""

"""
for temp in range(int(input())):
    l = int(input())
    s = str(input())

    set_l = len(set(s))
    print(len(set(s)))
    print(l)

    if(set_l == 1):
        print(l-1)
    elif(l == set_l):
        print(0)
    elif(l - set_l == 1):
        print(1)
    else:
        max_lim = l - set_l
        for i in range(l-max_lim):
            pass
        #print(l//set_l)
        pass

    print("-----------")
"""


"""
for temp in range(int(input())):
    l = int(input())
    s = str(input())

    set_l = len(set(s))
    print(len(set(s)))
    print(l)
    
    max_lim = l - set_l

    flag = 0
    for i in reversed(range(1,max_lim+1)):
        if(flag == 0):
            ind = 0
            for j in range(l-i+1):
                ss = s[ind:ind+i]
                #print(s[ind:ind+i])
                if(ss == ss[0]*len(ss)):
                    if(ss in s[ind+1:l]):
                        print(len(ss))
                        flag = 1
                        #print("_____")
                        break
                ind += 1
        else:
            break

    if(flag == 0):
        print(0)
    
    print("--------")
"""

"""
#dont use set (2.27 sec)

# 1.24 sec
for temp in range(int(input())):
    l = int(input())
    s = str(input())

    flag = 0
    for i in reversed(range(1,l)):
        if(flag == 0):
            ind = 0
            for j in range(l-i+1):
                ss = s[ind:ind+i]
                #print(s[ind:ind+i])
                if(ss == ss[0]*len(ss)):
                    if(ss in s[ind+1:l]):
                        print(len(ss))
                        flag = 1
                        #print("_____")
                        break
                ind += 1
        else:
            break

    if(flag == 0):
        print(0)
    #print("-----------------")
"""

"""
for temp in range(int(input())):
    l = int(input())
    s = str(input())
    
    #all_ss = []
    max_len = 0
    for i in range(l):
        for j in range(i+1,l+1):
            ss = s[i:j]
            rem = s[i+1:l]
            if(ss == ss[0]*len(ss)):
                if(ss in rem):
                    max_len = max(max_len, len(ss))

    print(max_len)     
"""

"""
    l2 = len(all_ss)
    #print(l2)

    all_ss_d = all_ss
    max_len = 0

    for i in range(l2):
        temp = all_ss[i]
        rem = all_ss[0:i] + all_ss[i+1:l2]
        if(temp in rem):
            #print(temp)
            max_len = max(max_len, len(temp))

    print(max_len)
    #print("-------------")
"""

"""
for temp in range(int(input())):
    l = int(input())
    s = str(input())
    
    all_ss = []
    for i in range(l):
        for j in range(i+1,l+1):
            ss = s[i:j]
            if(ss == ss[0]*len(ss)):
                all_ss.append(ss)
    
    #print(all_ss)
    # try sorting and check adjacent

    l2 = len(all_ss)
    #print(l2)

    all_ss_d = all_ss
    max_len = 0

    for i in range(l2):
        temp = all_ss[i]
        rem = all_ss[0:i] + all_ss[i+1:l2]
        if(temp in rem):
            #print(temp)
            max_len = max(max_len, len(temp))

    print(max_len)
    #print("-------------")
"""
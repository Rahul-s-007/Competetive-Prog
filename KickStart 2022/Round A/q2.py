import sys 
sys.stdin = open("C:\\Users\\LENOVO\\OneDrive\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\OneDrive\\Desktop\\Competetive Prog\\output.txt","w")

for temp in range(int(input())):
    inp = str(input())
    n = [int(x) for x in inp]
    pos = [(-1) for x in range(10)]
    s=0
    for i in range(len(n)):
        ele = n[i]
        s = s + ele
        if(pos[ele] < i):
            pos[ele] = i
    #print(pos)
    flag = 0
    s = 9 - (s%9)
    #print(s)
    #print(pos)
    ins = 0
    for i in range(10):
        if(flag == 0):
            if(pos[i] == -1):
                continue
            else:
                if(i<s):
                    ins = pos[i]+1
                elif(i==s):
                    pass
                else: # i>=s
                    if(pos[i]<ins):
                        ins = pos[i]
                #flag = 1
                #print(ins)
    print(f"Case #{temp+1}: {inp[:ins]+str(s)+inp[ins:]}")
    #if(flag == 0):
    #    print(f"Case #{temp+1}: {inp+str(s)}")
    #else:
    #    print(f"Case #{temp+1}: {inp[:ins]+str(s)+inp[ins:]}")
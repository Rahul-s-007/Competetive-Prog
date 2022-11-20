import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")

for temp in range(int(input())):
    l = int(input())
    t = str(input())
    b = [x for x in t]
    score=0
    for i in range(1,l):
        if(b[i-1]=="1"):
            if(b[i]=="0"):
                score=score+1
            else:
                b[i]="0"
        else:
            if(b[i]=="0"):
                score=score+1
            else:
                b[i]=1
    print(score)

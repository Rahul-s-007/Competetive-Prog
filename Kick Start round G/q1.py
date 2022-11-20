import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")

for temp in range(int(input())):
    t = [int(x) for x in input().split()]
    m=t[0] #total participants
    n=t[1] #number of days
    p=t[2] #p id of john
    board=[]
    ans=0
    for i in range(m):
        board.append([int(x) for x in input().split()])
    
    john = board[p-1]
    for i in range(n):
        max=0
        for j in range(m):
            if(john[i]<board[j][i]):
                diff = board[j][i]-john[i]
                if(max<diff):
                    max=diff
        ans=ans+max

    print(f"Case #{temp+1}: {ans}")
    #print(board)

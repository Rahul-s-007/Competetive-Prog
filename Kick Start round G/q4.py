import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")

for temp in range(int(input())):
    #n = int(input())
    t = [int(x) for x in input().split()]
    n = t[0]
    e = t[1]
    board = []
    face = 1 #right side
    same = 1 #same direction
    tenergy = 0
    posx = 0
    path_board = [[]]
    seg = 0

    for i in range(n):
        board.append([int(x) for x in input().split()])
    board.sort(key=lambda x: x[1],reverse = True)
    for i in range(n):
        if(i+1<n):
            if(board[i][1] == board[i+1][1]):
                path_board[seg].append(board[i])
            else:
                path_board[seg].append(board[i])
                seg += 1
                path_board.append([])
        else:
            path_board[seg].append(board[i])

    for i in range(len(path_board)):
        path_board[i].sort(key=lambda x: x[0])
    
    #print(path_board)

    def changeface(face):
        if(face == 1):
            return 0
        else:
            return 1

    #face = changeface(face)
    def checkdirection(p1,p2,face):
        if (face == 1):
            if(p2>p1):
                #print("same")
                return 1
            else:
                #print("opp")
                return 0
        else:
            if(p2>p1):
                #print("opp")
                return 0
            else:
                #print("same")
                return 1
    
    #same = checkdirection(board[pos][0],board[pos][1],face)
    x1 = 0
    x2 = 0
    for i in range(len(path_board)):
        for j in path_board[i]:
            x2 = j[0]
            #print(x2)
            same = checkdirection(x1,x2,face)
            if(same == 1):
                tenergy = tenergy + j[2]
            else:
                face = changeface(face)
                tenergy = tenergy + j[2] - e
            x1 = x2
    print(tenergy)

    #print(board)
    print("--------------------------")
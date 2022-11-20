import sys 
sys.stdin = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\input.txt","r")
sys.stdout = open("C:\\Users\\LENOVO\\Desktop\\Competetive Prog\\output.txt","w")

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1

row = len(image)
col = len(image[0])

samebit = image[sr][sc]
image[sr][sc]=2

color = 2

todo = [[sr,sc]]

visited = [[0 for _ in range(col)] for _ in range(row)]
visited[sr][sc] = 1

def ifvisited(m,n):
    if visited[m][n] == 0:
        return 1
    else:
        return 0

"""
def ifexists(m,n):
    if (0<=m and m<row and 0<=n and n<col):
        return 1
    else:
        return 0
"""

def up(m,n):
    i = m
    j = n-1

    if j >= 0:
        if(image[i][j] == samebit):
            if(ifvisited(i,j) == 1):
                image[i][j] = color
                todo.append([i,j])

def down(m,n):
    i = m
    j = n+1
    
    if j < col:
        if(image[i][j] == samebit):
            if(ifvisited(i,j) == 1):
                image[i][j] = color
                todo.append([i,j])

def left(m,n):
    i = m-1
    j = n
    
    if i >= 0:
        if(image[i][j] == samebit):
            if(ifvisited(i,j) == 1):
                image[i][j] = color
                todo.append([i,j])

def right(m,n):
    i = m+1
    j = n

    if i < row:
        if(image[i][j] == samebit):
            if(ifvisited(i,j) == 1):
                image[i][j] = color
                todo.append([i,j])

for coord in todo:
    m = coord[0]
    n = coord[1]
    up(m,n)
    down(m,n)
    left(m,n)
    right(m,n)

for _ in image:
    print(_)
#while(len(todo) != 0):

# up: i , j-1
# down: i , j+1
# right: i+1 , j
# left: i-1 , j
# limits: m-1,n-1
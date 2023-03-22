# import sys 
# sys.stdin = open("input.txt","r")
# sys.stdout = open("output.txt","w")

def is_legal(x,y,ele):
    # left_up x-1,y-1
    # up x,y-1
    # right_up x+1,y-1
    # left x-1,y
    # right x+1,y
    # left_dw x-1,y+1
    # down x,y+1
    # right_dw x+1,y+1
    #
    if(0<=x-1<n and 0<=y-1<n):
        if( abs(ele - arr[x-1][y-1]) > 1):
            pass
        else:
            return 0
    #
    if(0<=x<n and 0<=y-1<n):
        if( abs(ele - arr[x][y-1]) > 1):
            pass
        else:
            return 0
    #     
    if(0<=x+1<n and 0<=y-1<n):
        if( abs(ele - arr[x+1][y-1]) > 1):
            pass
        else:
            return 0
    #      
    if(0<=x-1<n and 0<=y<n):
        if( abs(ele - arr[x-1][y]) > 1):
            pass
        else:
            return 0
    
    #
    if(0<=x+1<n and 0<=y<n):
        if( abs(ele - arr[x+1][y]) > 1):
            pass
        else:
            return 0
    #        
    if(0<=x-1<n and 0<=y+1<n):
        if( abs(ele - arr[x-1][y+1]) > 1):
            pass
        else:
            return 0
    #
    if(0<=x<n and 0<= y+1<n):
        if( abs(ele - arr[x][y+1]) > 1):
            pass
        else:
            return 0
    #   
    if(0<=x+1<n and 0<= y+1<n):
        if( abs(ele - arr[x+1][y+1]) > 1):
            pass
        else:
            return 0
    
    return 1


for temp in range(int(input())):
    n = int(input())
    arr = [[-1 for i in range(n)] for j in range(n)]
    possible = [i for i in range(n*n)]
    print("DONE")
    
    rowStart = 0
    rowEnd = n-1
    colStart = 0
    colEnd = n-1
    
    while(rowStart<=rowEnd and colStart<=colEnd):
        for i in range(colStart,colEnd+1):
            #print(arr[rowStart][i])
            #print(i,j)
            filled = 0
            while (filled == 0):
                for ind,ele in enumerate(possible):
                    if(is_legal(rowStart,i,ele)):
                        print(ele)
                        arr[rowStart][i] = ele
                        filled = 1
                        possible.pop(ind)
                        break
        rowStart += 1
        
        for i in range(rowStart,rowEnd+1):
            #print(arr[i][colEnd])
            #print(i,j)
            filled = 0
            while (filled == 0):
                for ind,ele in enumerate(possible):
                    if(is_legal(i,colEnd,ele)):
                        print(ele)
                        arr[i][colEnd] = ele
                        filled = 1
                        possible.pop(ind)
                        break
        colEnd -= 1
        
        if(rowStart<=rowEnd):
            for i in range(colEnd,colStart-1,-1):
                #print(arr[rowEnd][i])
                #print(i,j)
                filled = 0
                while (filled == 0):
                    for ind,ele in enumerate(possible):
                        if(is_legal(rowEnd,i,ele)):
                            print(ele)
                            arr[rowEnd][i] = ele
                            filled = 1
                            possible.pop(ind)
                            break
            rowEnd -= 1
            
        if(colStart<=colEnd):
            for i in range(rowEnd,rowStart-1,-1):
                #print(arr[i][colStart])
                #print(i,j)
                filled = 0
                while (filled == 0):
                    for ind,ele in enumerate(possible):
                        if(is_legal(i,colStart,ele)):
                            print(ele)
                            arr[i][colStart] = ele
                            filled = 1
                            possible.pop(ind)
                            break
            colStart += 1

    for i in arr:
        for j in i:
            print(j+1, end = " ")
        print()
        
"""
import random
def generate_matrix(n):
    matrix = [[0 for x in range(n)] for y in range(n)]
    used_numbers = set()

    for i in range(n):
        for j in range(n):
            while True:
                num = random.randint(1, n*n)
                if num not in used_numbers and (i == 0 or abs(num - matrix[i-1][j]) > 1) and (j == 0 or abs(num - matrix[i][j-1]) > 1):
                    matrix[i][j] = num
                    used_numbers.add(num)
                    break

    return matrix
""" 

"""
One approach to solve this problem is to use a modified version of the spiral matrix construction algorithm.
The basic idea is to start with the center of the matrix and then spiral outwards while filling in each cell 
with the next available integer. To ensure that the absolute difference between neighbouring cells is greater than 1,
we can keep track of the last value placed and check that the absolute difference is at least 2 before placing the next value.
Here's the Python code:
"""

"""
def generate_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    center = (n // 2, n // 2)
    current = 1
    last = None
    direction = 0 # 0:right, 1:down, 2:left, 3:up
    steps = 1
    while current <= n * n:
        x, y = center
        if direction == 0:
            y += steps
        elif direction == 1:
            x += steps
        elif direction == 2:
            y -= steps
        else:
            x -= steps
        if 0 <= x < n and 0 <= y < n and matrix[x][y] == 0:
            if last is None or abs(current - last) > 1:
                print(current)
                matrix[x][y] = current
                last = current
                current += 1
            else:
                # cannot place this value, switch to next direction
                direction = (direction + 1) % 4
        else:
            # cannot move in current direction, switch to next direction
            direction = (direction + 1) % 4
            if direction == 0:
                steps += 1
    return matrix

print(generate_matrix(4))
"""
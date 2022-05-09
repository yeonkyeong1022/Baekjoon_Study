import sys 
from collections import deque

M, N = map(int, input().split())
T = [] 
for i in range(N):
    T.append(list(map(int, sys.stdin.readline().split())))

    
def bfs():  
    global queue
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    x=0
    y=0    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue 
            if T[nx][ny] == -1 or T[nx][ny] == 1:
                continue 
            if T[nx][ny] == 0:
                T[nx][ny] = T[x][y] + 1
                queue.append((nx, ny))
    return T[x][y]-1

queue = deque()             
for i in range(N):
    for j in range(M):
        if T[i][j]==1:
            queue.append((i, j))
            
result = bfs()

for i in range(N):
    for j in range(M):
        if T[i][j] == 0:
            result = -1
print(result)
import sys 
from collections import deque 

M, N, H = map(int, input().split())
T = []
for i in range(H):
    t = []
    for j in range(N):
        t.append(list(map(int, sys.stdin.readline().split())))
    T.append(t)
    
queue = deque()

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0] 
dz = [0, 0, 0, 0, -1, 1]
for i in range(H):
    for j in range(N):
        for k in range(M):
            if T[i][j][k] == 1:
                queue.append((i, j, k))

def bfs():
    x = 0
    y = 0
    z = 0 
    global queue 
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            if nx<0 or nx>=H or ny<0 or ny>=N or nz<0 or nz>= M:
                continue
            if T[nx][ny][nz] == -1 or T[nx][ny][nz] == 1:
                continue 
            if T[nx][ny][nz] == 0:
                T[nx][ny][nz] = T[x][y][z]+1 
                queue.append((nx, ny, nz))
    return T[x][y][z]-1 

result = bfs()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if T[i][j][k] == 0:
                result = -1
print(result)
        
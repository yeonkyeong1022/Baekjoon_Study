from collections import deque 
from sys import stdin 
import copy 

N, M = map(int, stdin.readline().split())
L = [list(map(int, stdin.readline().split())) for _ in range(N)]

queue = deque()
Max = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 
def bfs():
    global Max 
    cL = copy.deepcopy(L)
    for i in range(N):
        for j in range(M):
            if cL[i][j] == 2:
                queue.append([i,j])
    while queue:
        x, y = queue.popleft() 
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if cL[nx][ny] == 0:
                    cL[nx][ny] = 2
                    queue.append([nx, ny])
    cnt = 0
    for i in cL:
        cnt+=i.count(0)
    Max = max(Max, cnt)

def wall(x):
    if x==3:
        bfs()
        return 
    for i in range(N):
        for j in range(M):
            if L[i][j] == 0:
                L[i][j] = 1
                wall(x+1)
                L[i][j] = 0

wall(0)
print(Max)
    
    
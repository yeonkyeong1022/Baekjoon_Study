# [토마토](https://www.acmicpc.net/problem/7576)

| 시간 제한 | 메모리 제한 | 난이도 |
| --- | --- | --- |
| 1 초 | 256 MB | gold 5 |

## 문제

> 철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다.
> 
> 
> 창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.
> 
> 토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
> 

## 입력

> 첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M,N ≤ 1,000 이다. 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다. 하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
> 
> 
> 토마토가 하나 이상 있는 경우만 입력으로 주어진다.
> 

## 출력

> 여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
> 

## Code

```python
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
```

- BFS를 사용하여 해결 : 0인 노드 끼리 이어진 그래프라고 생각한다.(시작점은 1)
- 큐를 활용한다. 모든 그래프를 돌아 1인 지점의 좌표들을 먼저 큐에 넣고 시작한다.
    - 함수 내에서 큐 앞부분에서 빼낸 좌표(처음에 1이었던 좌표)를 기준으로 상하좌우 탐색
    - 만약 토마토가 없거나(-1) 이미 익어있다면(1) 스킵
    - 익지 않았다면 해당 토마토를 익게 만들고 몇 번째로 익었는지 값을 매겨준다.
        
        ( `T[nx][ny] = T[x][y] + 1` )
        
    - 시작점의 토마토가 0번째로 익은 토마토이므로 return 할 땐 1씩 빼주어야 한다
- 주의할 점 :
    - 처음부터 큐에 아무것도 들어있지 않은 경우 : 토마토가 모두 안익은 상태일 경우
        - while문을 돌지 않고 바로 return 하므로 x, y를 0으로 미리 초기화시켜주어야 한다. (그렇지 않으면 UnboundLocalError가 뜨더라)
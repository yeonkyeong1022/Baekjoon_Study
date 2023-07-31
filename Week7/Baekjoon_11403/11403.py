from sys import stdin 
import heapq

N = int(stdin.readline())
G = []
graph = [[] for i in range(N)]

for i in range(N):
    G.append(list(map(int, input().split())))
    for j in range(N):
        if G[i][j] == 1:
            graph[i].append(j)

def bfs(start):
    distance = [0]*(N)
    q = []
    heapq.heappush(q, start)
    distance[start] = 0
    while q:
        now = heapq.heappop(q)
        for i in graph[now]:
            if distance[i] == 0:
                distance[i] = 1
                heapq.heappush(q, i)
    for i in range(N):
        print(distance[i], end=' ')
    print()
    
for i in range(N):
    bfs(i)
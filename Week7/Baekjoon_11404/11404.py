import sys
import heapq 
input = sys.stdin.readline 
INF = int(1e9)

n = int(input())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)
G = []

for i in range(n):
    G.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if G[i][j] == 1:
            graph[i].append((j, 1))
        else :
            graph[i].append((j, INF))

def dijkstra(start):
    q = [] 
    heapq.heappush(q, (INF, start))
    distance[start] = INF
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<dist :
            continue 
        for i in graph[now]:
            cost = 1 
            if cost < distance[i[0]]:
                distance[i[0]] = cost 
                heapq.heappush(q, (cost, i[0]))

for i in range(n):
    distance = [INF]*(n+1)
    dijkstra(i)
    for j in range(n):
        if distance[j]==INF:
            print(0, end=' ')
        else :
            print(1, end=' ')
    print()

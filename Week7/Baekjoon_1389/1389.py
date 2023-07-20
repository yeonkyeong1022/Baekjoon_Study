import sys
import heapq 
input = sys.stdin.readline 
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)
            
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    

def dijkstra(start):
    q = [] 
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<dist :
            continue 
        for i in graph[now]:
            cost = dist +i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost 
                heapq.heappush(q, (cost, i[0]))

min = INF 
for i in range(1, n+1):
    distance = [INF]*(n+1)
    dijkstra(i)
    print(distance)
    sum = 0
    for j in range(1, n+1):
        if distance[j] != INF:
            sum += distance[j]
    if min>sum:
        min = sum 
print(min)
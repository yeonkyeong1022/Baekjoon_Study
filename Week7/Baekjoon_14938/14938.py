import sys 
import heapq 
input = sys.stdin.readline 
# INF = 2000
INF = int(1e9)
n, m, r = map(int, input().split())
t = list(map(int, input().split()))
t = [0]+t
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)
for i in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

# print("t:", t)
def dijkstra(start):
    q = []
    heapq.heappush(q, (start, 0))
    distance[start] = 0
    while q:
        now, dist = heapq.heappop(q)
        # print(now, dist)
        if distance[now] <dist:
            continue 
        for i in graph[now]:
            cost = dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost 
                heapq.heappush(q, (i[0], cost))
    totalItem = 0
    # print(distance)
    for i in range(1,n+1):
        if distance[i] <= m:
            totalItem += t[i]
    return totalItem
maxItem = 0
for i in range(1, n+1):
    distance = [INF]*(n+1)
    tmp = dijkstra(i)
    if tmp>maxItem:
        maxItem = tmp 
print(maxItem)

 
    
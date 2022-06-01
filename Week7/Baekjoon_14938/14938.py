import sys 
import heapq 
input = sys.stdin.readline 
INF = int(1e9)

N = int(input())

graph = [[0] for i in range(N+1)]

for i in range(1, N+1):
    graph[i].append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == 0:
            graph[i][j] = INF 
        if i==j :
            graph[i][j] = 0 

print(graph)
    

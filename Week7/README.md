# 이코테 강의 07.

# 최단 경로 알고리즘

**최단 경로 알고리즘은 다음의 여러 문제 상황에서 사용될 수 있다.**

- 한 지점에서 다른 한 지점까지의 최단 경로
- 한 지점에서 다른 모든 지점까지의 최단 경로(다익스트라?)
- 모든 지점에서 다른 모든 지점까지의 최단 경로(아마 크루스칼)

※각 지점은 그래프에서 **노드(Vertex)**로 표현하고 연결된 도로를 **간선(Edge)**으로 표현

## 다익스트라(Dijkstra) 최단경로 알고리즘

- 특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로 계산
- 음의 간선이 없을 때 정상적으로 작동한다
- 그리디 알고리즘으로 분류된다.
    - **매 상황에서 가장 비용이 적은 노드를 선택**

**동작 과정**

- 최단 거리 테이블은 각 노드에 대한 현재까지의 최단 거리 정보를 가진다.
- 처리 과정에서 더 짧은 경로를 찾으면 테이블에서 해당 노드까지의 **최단 거리를 갱신**한다

```python
from sys import stdin 
INF = int(1e9)

n, m = map(int, input().split()) 

start = int(input()) 

graph = [[] for i in range(n+1)] 
visited = [False]*(n+1) 
distance = [INF]*(n+1) 

for _ in range(m):
    a, b, c = map(int, input().split()) 
    graph[a].append((b, c)) 

def get_smallest_node():
    min_value = INF 
    index=0 
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            index = i 
    return index 

def dijkstra(start):
    distance[start] = 0 
    visited[start] = True 
    for j in graph[start]:
        distance[j[0]] = j[1] 
    for i in range(n-1):
        now = get_smallest_node() 
        visited[now] = True 
        for j in graph[now]:
            cost = distance[now]+j[1] 
            if cost<distance[j[0]]:
                distance[j[0]] = cost 
                
dijkstra(start) 

for i in range(1, n+1):
    if distance[i] == INF :
        print("Infinity")
    else :
        print(distance[i])
```

- 시간 복잡도:
    - 총 O(v) 번에 걸쳐 최단거리가 가장 짧은 노드를 매번 선형 탐색
    - 전체 시간 복잡도: $O(V^2)$
    - ㅅ시간복잡도가 높아 많은 데이터에는 적합하지 않다

## 우선순위 큐(Priority Queue

: 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조

### 힙 라이브러리

```python
import heapq 

def heapsort(iterable):
    h=[] 
    result = [] 
    for value in iterable:
        heapq.heappush(h, value) 
    for i in range(len(h)):
        result.append(heapq.heappop(h)) 
    return result 

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
```

- 우선순위 큐를 활용해 다익스트라 알고리즘 구현
    - 그래프를 준비하고 출발노드를 설정하여 우선순위 큐에 삽입한다.
    - 우선순위 큐에서 원소를 꺼내 방문 여부에 따라 처리한다.
    
    ```python
    import heapq 
    INF = int(1e9) 
    
    n, m = map(int, input()) 
    start = int(input()) 
    
    graph = [[] for i in range(n+1)] 
    
    distance = [INF]*(n+1) 
    
    for _ in range(m):
        a, b, c, = map(int, input().split())
        graph[a].append((b, c)) 
        
    def dijkstra(start):
        q=[] 
        heapq.heappush(0, start)
        distance[start] = 0 
        while q:
            dist, now = heapq.heappop(q) 
            if distance[now]<dist:
                continue 
            for i in graph[now]:
                cost = dist+i[1]
                if cost <distance[i[0]]:
                    distance[i[0]] = cost 
                    heapq.heappush(q, (cost, i[0])) 
    dijkstra(start) 
    
    for i in range(1, n+1):
        if distance[i] == INF :
            print("infinity") 
        else:
            print(distance[i])
    ```
    
    - 힙 자료구조를 사용하는 다익스트라 시간 복잡도 : $O(ElogV)$
    

## 플로이드 워셜 알고리즘

: 각 단계마다 특정한 노드 k를 거쳐가는 경우를 확인

- a에서 b로 가는 최단거리보다 a에서 k를 거쳐 b로 가는 거리가 더 짧으지 검사
- 점화식:
    - $D_{ab} = min(D_{ab}, D_{ak}+D_{kb})$
1. 그래프를 준비하고 최단거리 테이블을 초기화한다
2. n번 노드를 거쳐가는 경우를 고려하여 테이블을 갱신한다
    
    ```python
    INF = int(1e9) 
    
    n = int(input()) 
    m = int(input())
    
    graph = [[INF]*(n+1) for _ in range(n+1)]
    
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a==b:
                graph[a][b] = 0 
    
    for _ in range(m):
        a, b, c = map(int, input(). split())
        graph[a][b] = c 
    
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b]) 
    
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][b] == INF:
                print("Infinity", end=" ")
            else: 
                print(graph[a][b], end= " ")
        print()
    ```
    
    - 시간 복잡도 : $O(N^3)$ 짱길다~
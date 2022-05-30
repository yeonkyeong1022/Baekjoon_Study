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

### 문제 : 전보

- 문제 설명
    - 어떤 나라에는 N개의 도시가 있다. 그리고 각 도시는 보내고자 하는 메시지가 있는 경우, 다른 도시로 전보를 보내서 다른 도시로 해당 메시지를 전송할 수 있다.
    - 하지만 X라는 도시에서 Y라는 도시로 전보를 보내고자 한다면, 도시 X에서 Y로 향하는 통로가 설치되어 있어야 한다. 예를 들어 X에서 Y로 향하는 통로는 있지만, Y에서 X로 향하는 통로가 없다면 Y는 X로 메시지를 보낼 수 없다. 또한 통로를 거쳐 메시지를 보낼 때는 일정 시간이 소요된다.
    - 어느 날 C라는 도시에서 위급 상황이 발생했다. 그래서 최대한 많은 도시로 메시지를 보내고자 한다. 메시지는 도시 C에서 출발하여 각 도시 사이에 설치된 통로를 거쳐, 최대한 많이 퍼져나갈 것이다.
    - 각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때, 도시 C에서 보낸 메시지를 받게 되는 도시의 개수는 총 몇 개이며 도시들이 모두 메시지를 받는 데까지 걸리는 시간은 얼마인지 계산하는 프로그램을 작성하시오.
- 문제 조건
    - 풀이 시간 60분 | 시간 제한 1초 | 메모리 제한 128MB
    - 입력 조건
        - 첫째 줄에 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C가 주어진다.(1≤N≤30,000 , 1≤Z≤ 1,000 , 1 ≤ C ≤ N)
        - 둘째 줄부터 M+1번째 줄에 걸쳐서 통로에 대한 정보 X, Y, Z가 주어진다. 이는 특정 도시 X에서 다른 특정 도시 Y로 이어지는 통로가 있으며, 메시지가 전달되는 시간이 Z라는 의미다.(1 ≤ X, Y ≤ N , 1≤ Z ≤ 1,000)
    - 출력 조건
        - 첫째 줄에 도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간을 공백으로 구분하여 출력한다.
    - 입력예시
        
        ```python
        3 2 1
        1 2 4
        1 3 2
        ```
        
    - 출력예시
        
        ```python
        2 4
        ```
        
    - 답안 예시
        
        ```python
        import heapq
        import sys 
        input = sys.stdin.readline 
        INF = int(1e9)
        
        n, m, start = map(int, input().split())
        graph = [[] for i in range(n+1)]
        distance = [INF]*(n+1)
        
        for _ in range(m):
            x, y, z = map(int, input().split())
            graph[x].append((y, z))
        
        def dijkstra(start):
            q=[]
            heapq.heappush(q, (0, start))
            distance[start]=0 
            while q:
                dist, now = heapq.heappop(q)
                if distance[now] < dist:
                    continue 
                for i in graph[now]:
                    cost = dist + i[1] 
                    if cost<distance[i[0]]:
                        distance[i[0]] = cost 
                        heapq.heappush(q, (cost, i[0]))
        
        dijkstra(start)
        count=0
        max_distance = 0
        for d in distance:
            if d != 1e9:
                count += 1
                max_distance = max(max_distance, d)
        
        print(count-1, max_distance)
        ```
        

### 문제: 미래도시

- 문제 설명
    - 미래도시에는 1번부터 N번까지의 회사가 있는데 특정 회사끼리는 서로 도로를 통해 연결되어 있다. 방문 판매원 A는 현재 1번 회사에 위치해 있으며, X번 회사에 방문해 물건을 판매하고자 한다.
    - 미래도시에서 특정 회사에 돡하기 위한 방법은 회사끼리 연결되어 있는 도로를 이용하는 방법이 유일하다. 또한 연결된 2개의 회사는 양방향으로 이동할 수 있다. 공중 미래 도시에서 특정 회사와 다른 회사가 도로로 연결되어 있다면, 정확히 1만큼의 시간으로 이동할 수 있다.
    - 또한 오늘 방문 판매원 A는 기대하던 소개팅에도 참석하고자 한다. 소개팅의 상대는 K번 회사에 존재한다. 방문 판매원 A는 X번 회사에 가서 물건을 판매하기 전에 먼저 소개팅 상대의 회사에 찾아가서 함께 커피를 마실 예정이다. 따라서 방문 판매원 A는 1번 회사에서 출발하여 K번 회사를 방문한 뒤에 X번 회사로 가는 것이 목표다. 이 때 방문 판매원 A는 가능한 한 빠르게 이동하고자 한다.
    - 방문 판매원이 회사 사이를 이동하게 되는 최소 시간을 계산하는 프로그램을 작성하시오.
- 문제 조건:
    - 풀이시간 40분 | 시간 제한 1초 | 메모리 제한 128MB
    - 입력 조건:
        - 첫째 줄에 전체 회사의 개수 N과 경로의 개수 M이 공백으로 구분되어 차례대로 주어진다. (1 ≤ N, M ≤ 100)
        - 둘째 줄부터 M+1번째 줄에는 연결되 두 회사의 번호가 공백으로 구분되어 주어진다.
        - M+2번째 줄에는 X와 K가 공백으로 구분되어 차례대로 주어진다. (1 ≤ K ≤ 100)
    - 출력 조건:
        - 첫째 줄에 방문 판매원 A가 K번 회사를 거쳐 X번 회사로 가는 최소 이동 시간을 출력한다.
        - 만약 X번 회사에 도달할 수 없다면 -1을 출력한다
    - 입력 예시
        
        ```python
        5 7
        1 2
        1 3
        1 4
        2 4
        3 4
        3 5
        4 5
        4 5
        ```
        
    - 출력 예시
        
        ```python
        3
        ```
        
    
    - 문제 해결
        - 최단 거리 알고리즘을 이용해 해결한다
        - N의 크기가 최대 100이므로 플로이드 워셜 알고리즘을 이용할 수도 있다.
            
            ```python
            INF = int(1e9)
            
            n, m = map(int, input().split())
            graph = [[INF]*(n+1) for _ in range(n+1)]
            
            for a in range(1, n+1):
                for b in range(1, n+1):
                    if a==b:
                        graph[a][b] = 0 
            
            for _ in range(m):
                a, b = map(int, input().split())
                graph[a][b] = 1 
                graph[b][a] = 1
            
            x, k = map(int, input().split())
            
            for k in range(1, n+1):
                for a in range(1, n+1):
                    for b in range(1, n+1):
                        graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
            
            distance = graph[1][k] + graph[k][x]
            
            if distance >= INF:
                print("-1")
            else:
                print(distance)
            ```
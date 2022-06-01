# 

# [최소비용 구하기](https://www.acmicpc.net/problem/1916)

| 시간 제한 | 메모리 제한 | 난이도 |
| --- | --- | --- |
| 0.5 초 | 128 MB | gold 5 |

## 문제

N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다. 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N까지이다.

## 입력

첫째 줄에 도시의 개수 N(1 ≤ N ≤ 1,000)이 주어지고 둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)이 주어진다. 그리고 셋째 줄부터 M+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.

그리고 M+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다. 출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어진다.

## 출력

첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.

---

## Code

```python
import sys 
import heapq 
input = sys.stdin.readline 
N = int(input())
M = int(input())

INF = int(1e9)
graph = [[] for i in range(N+1)]
distance = [INF]*(N+1)

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) 
    
start, end = map(int, input().split())

def dijkstra(start):
    q = [] 
    heapq.heappush(q,(0,  start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost 
                heapq.heappush(q, (cost, i[0]))
dijkstra(start) 

print(distance[end])
```

- 힙 자료구조를 이용한 다익스트라 알고리즘을 사용했다.
- 이코테 영상 강의를 정리한 페이지에서 똑같이 설명했기 때문에 별다른 코멘트를 추가할게 없다. 쩝,,~
- 중간중간 헷갈렸던게  N만큼 반복할지 M만큼 곱해줄지 등등 이었으니 그정도만 정리하자.
    - `graph = [[] for i in range(N+1)]` : 도시(노드)의 개수만큼 만들어야 한다. 출발도시와 도착도시를 표시할 수 있는 이차원 배열이므로 NxN의 크기이다.(0번째는 사용x)
    - `distance = [INF]*(N+1)` : 목적지 도시까지의 버스 비용이므로 도시 개수만큼 만들어준다.
# 경로 찾기

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 256 MB | 42324 | 25557 | 18811 | 60.170% |

## 문제

가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 정점의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄부터 N개 줄에는 그래프의 인접 행렬이 주어진다. i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재한다는 뜻이고, 0인 경우는 없다는 뜻이다. i번째 줄의 i번째 숫자는 항상 0이다.

## 출력

총 N개의 줄에 걸쳐서 문제의 정답을 인접행렬 형식으로 출력한다. 정점 i에서 j로 가는 길이가 양수인 경로가 있으면 i번째 줄의 j번째 숫자를 1로, 없으면 0으로 출력해야 한다.

---

## 문제 풀이

```python
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
```

- bfs를 사용하여 풀 수 있다. bfs에 대한 자세한 알고리즘 설명은 생략하도록 하겠다.
- distance 변수를 bfs 함수 내에서 정의하고 그때그때 출력하도록 한다.
    - start 지점에서 시작하여 다른 정점까지 도달할 수 있으면 1, 그렇지 않으면 0을 기록하는 1차원 배열이다.
    - bfs 탐색을 통해 start부터 다른 점까지 최단 경로를 구하여 1을 저장한다.
- bfs 탐색이 끝나면 distance 변수 결과값을 출력하고 함수를 빠져나온다. 이 함수를 N번 반복한다. 결과적으로 모든 정점에서 다른 정점까지 도달할 수 있는지 0과 1로 표현하는 행렬이 출력된다.
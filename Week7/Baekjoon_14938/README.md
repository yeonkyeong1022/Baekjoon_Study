# 서강그라운드

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 1 초 | 128 MB | 10969 | 5707 | 4601 | 50.483% |

## 문제

예은이는 요즘 가장 인기가 있는 게임 서강그라운드를 즐기고 있다. 서강그라운드는 여러 지역중 하나의 지역에 낙하산을 타고 낙하하여, 그 지역에 떨어져 있는 아이템들을 이용해 서바이벌을 하는 게임이다. 서강그라운드에서 1등을 하면 보상으로 치킨을 주는데, 예은이는 단 한번도 치킨을 먹을 수가 없었다. 자신이 치킨을 못 먹는 이유는 실력 때문이 아니라 아이템 운이 없어서라고 생각한 예은이는 낙하산에서 떨어질 때 각 지역에 아이템 들이 몇 개 있는지 알려주는 프로그램을 개발을 하였지만 어디로 낙하해야 자신의 수색 범위 내에서 가장 많은 아이템을 얻을 수 있는지 알 수 없었다.

각 지역은 일정한 길이 l (1 ≤ l ≤ 15)의 길로 다른 지역과 연결되어 있고 이 길은 양방향 통행이 가능하다. 예은이는 낙하한 지역을 중심으로 거리가 수색 범위 m (1 ≤ m ≤ 15) 이내의 모든 지역의 아이템을 습득 가능하다고 할 때, 예은이가 얻을 수 있는 아이템의 최대 개수를 알려주자.

![Alt text](https://upload.acmicpc.net/ef3a5124-833a-42ef-a092-fd658bc8e662/-/preview/)

주어진 필드가 위의 그림과 같고, 예은이의 수색범위가 4라고 하자. ( 원 밖의 숫자는 지역 번호, 안의 숫자는 아이템 수, 선 위의 숫자는 거리를 의미한다) 예은이가 2번 지역에 떨어지게 되면 1번,2번(자기 지역), 3번, 5번 지역에 도달할 수 있다. (4번 지역의 경우 가는 거리가 3 + 5 = 8 > 4(수색범위) 이므로 4번 지역의 아이템을 얻을 수 없다.) 이렇게 되면 예은이는 23개의 아이템을 얻을 수 있고, 이는 위의 필드에서 예은이가 얻을 수 있는 아이템의 최대 개수이다.

## 입력

첫째 줄에는 지역의 개수 n (1 ≤ n ≤ 100)과 예은이의 수색범위 m (1 ≤ m ≤ 15), 길의 개수 r (1 ≤ r ≤ 100)이 주어진다.

둘째 줄에는 n개의 숫자가 차례대로 각 구역에 있는 아이템의 수 t (1 ≤ t ≤ 30)를 알려준다.

세 번째 줄부터 r+2번째 줄 까지 길 양 끝에 존재하는 지역의 번호 a, b, 그리고 길의 길이 l (1 ≤ l ≤ 15)가 주어진다.

지역의 번호는 1이상 n이하의 정수이다. 두 지역의 번호가 같은 경우는 없다.

---

## 문제 풀이

```python
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

		###### 따로 처리해야 할 부분 ######
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
```

- 코드가 길어 복잡해보이지만 핵심은 가운데 정의한 dijkstra 함수이다.
- 이코테 강의에서 설명한 코드와 크게 다르지 않다. 우선순위 힙을 활용하여 다익스트라 구현한 파트에서 거의 코드를 그대로 가져왔다고 봐도 무방하다. 추가해준 지점은 함수 아래 while 문을 빠져나온 뒤 처리해준 부분이다.
    - 수색 범위 내에서 가질 수 있는 아이템의 최대 개수를 구해야 한다. 따라서 수색범위 m 보다 거리가 작은 경우 해당 정점 번호에 해당하는 아이템의 개수를 totalItem 변수에 합쳐준다.
    - totalItem을 최종적으로 반환해준다. 함수를 1부터 n까지 반복하여 그 중 totalItem의 최대값을 구하여 출력해주면 해결된다.
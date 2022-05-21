# [먹을 것인가 먹힐 것인가](https://www.acmicpc.net/problem/7795)

| 시간 제한 | 메모리 제한 | 난이도 |
| --- | --- | --- |
| 1 초 | 256 MB | silver 3 |

## 문제

> 심해에는 두 종류의 생명체 A와 B가 존재한다. A는 B를 먹는다. A는 자기보다 크기가 작은 먹이만 먹을 수 있다. 예를 들어, A의 크기가 {8, 1, 7, 3, 1}이고, B의 크기가 {3, 6, 1}인 경우에 A가 B를 먹을 수 있는 쌍의 개수는 7가지가 있다. 8-3, 8-6, 8-1, 7-3, 7-6, 7-1, 3-1.
> 
> 
> 두 생명체 A와 B의 크기가 주어졌을 때, A의 크기가 B보다 큰 쌍이 몇 개나 있는지 구하는 프로그램을 작성하시오.
> 

## 입력

> 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 A의 수 N과 B의 수 M이 주어진다. 둘째 줄에는 A의 크기가 모두 주어지며, 셋째 줄에는 B의 크기가 모두 주어진다. 크기는 양의 정수이다. (1 ≤ N, M ≤ 20,000)
> 

## 출력

> 각 테스트 케이스마다, A가 B보다 큰 쌍의 개수를 출력한다.
> 

## Code

```python
import sys
from bisect import bisect_left, bisect_right
T = int(input())
for i in range(T):
    cnt = 0
    N, M = map(int, input().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))

    A.sort()
    B.sort()
    
    for i in range(N):
        cnt += bisect_left(B, A[i])

    print(cnt)
```

- `bisect` 모듈 : 이진탐색 알고리즘에 사용되는 모듈. 실전에서 유용하게 사용된다.
    - `bisect_left(B, A[i])` : 정렬된 B 리스트에서 A[i] 값이 들어갈 위치의 인덱스를 반환한다.
        
        ⇒리스트 B의 원소들 중 A[i]보다 작은 원소의 개수를 반환하게 된다.
        
- 문제에서 요구하는 쌍의 개수를 `cnt`로 두고 반복문을 돌려 A[i]보다 작은 B의 원소들의 쌍의 개수를 cnt에 더한다.
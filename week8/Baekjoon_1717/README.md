# 집합의 표현

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 128 MB | 84780 | 26900 | 16314 | 28.134% |

## 문제

초기에 $n+1$개의 집합 $\{0\}, \{1\}, \{2\}, \dots , \{n\}$이 있다. 여기에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고 한다.

집합을 표현하는 프로그램을 작성하시오.

## 입력

첫째 줄에 n, $m$이 주어진다. m은 입력으로 주어지는 연산의 개수이다. 다음 m개의 줄에는 각각의 연산이 주어진다. 합집합은 0 a b의 형태로 입력이 주어진다. 이는 a가 포함되어 있는 집합과, b가 포함되어 있는 집합을 합친다는 의미이다. 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은 1 a b의 형태로 입력이 주어진다. 이는 a와 b가 같은 집합에 포함되어 있는지를 확인하는 연산이다.

## 출력

1로 시작하는 입력에 대해서 a와 b가 같은 집합에 포함되어 있으면 "`YES`" 또는 "`yes`"를, 그렇지 않다면 "`NO`" 또는 "`no`"를 한 줄에 하나씩 출력한다.

## 제한

- 1 ≤ n ≤ 1,000,000
- 1 ≤ m ≤ 100,000
- 0 ≤ a, b ≤ n
- a, b는 정수
- a와 b는 같을 수도 있다.

---

## 문제 풀이

```python
from sys import stdin, setrecursionlimit
setrecursionlimit(100000)

def Find(parent, x):
    if parent[x] != x:
        parent[x] = Find(parent, parent[x])
    return parent[x]

def Union(parent, a, b):
    a = Find(parent, a)
    b = Find(parent, b)
    if a>b:
        parent[a] = b 
    else:
        parent[b] = a

n, m = map(int, stdin.readline().split())
parent = [0]*(n+1)
for i in range(1, n+1):
    parent[i] = i 

for _ in range(m):
    uf, a, b = map(int, stdin.readline().split()) # uf: union할지 find할지 확인
    if uf == 1:
        if Find(parent, a) == Find(parent, b):
            print("YES")
        else:
            print("NO")
    else :
        Union(parent, a, b)
```

- 이코테 강의에서 설명한 Union-Find 함수를 그대로 사용하여 풀 수 있다.
- 나머지는 입력과 출력, 함수의 반환값으로 처리해주는 것 뿐이라 union-find의 개념만 알면 브론즈만큼 쉬운 문제이다.
- python의 경우 재귀함수가 1000번으로 제한되어있으므로 제출할 때 sys.setrecurtsionlimit()로 제한을 늘려주어야 한다. 그렇지않으면 런타임 에러가 발생
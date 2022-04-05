# [행렬](https://www.acmicpc.net/problem/1080)

| 시간 제한 | 메모리 제한 | 난이도 |
| --- | --- | --- |
| 2 초 | 128 MB | silver 1 |

## 문제

> 0과 1로만 이루어진 행렬 A와 행렬 B가 있다. 이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오.
> 
> 
> 행렬을 변환하는 연산은 어떤 3×3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 → 1, 1 → 0)
> 

## 입력

> 첫째 줄에 행렬의 크기 N M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 행렬 A가 주어지고, 그 다음줄부터 N개의 줄에는 행렬 B가 주어진다.
> 

## 출력

> 첫째 줄에 문제의 정답을 출력한다. 만약 A를 B로 바꿀 수 없다면 -1을 출력한다.
> 

## Code

```python
import sys 
A = []
B = []
cnt = 0

def Swap(A, i, j):                                 # a
    for I in range(3):
        for J in range(3):
            A[I+i][J+j] = int(not A[I+i][J+j])
    
n, m = map(int, input().split())
for i in range(n):
    A.append(list(map(int, list(sys.stdin.readline().rstrip())))) 

for i in range(n):
    B.append(list(map(int, list(sys.stdin.readline().rstrip()))))
    
for i in range(n-2):
    for j in range(m-2):
        if A[i][j]!=B[i][j]:                     # b
            Swap(A, i, j)
            cnt += 1
if A==B:                                         # c
    print(cnt)
else :
    print(-1)
```

- 이 문제는 복잡해보이지만 풀이과정을 요약하면 다음과 같다
    1. 행렬 A의 어떤 한 위치의 값이 행렬 B와 다르다면 3*3행렬변환을 하고 아니면 냅둔다.
    2. 1의 과정을 행렬 처음부터 끝(마지막에서 3번째칸)까지 돌린다.
    3. 이 과정을 거친 후 A와 B가 같아졌는지 확인한다.
- 행렬을 입력받을 때 뒤에 `rstrip()` 함수를 써주었다. 그렇게 해야만 뒤에 ‘\n’이 빠져나가 정상적으로 int로 변환할 수 있다.(`sys.stdin.readline()` 의 경우 ‘\n’까지 입력받는다)
- 전체적인 과정:
    1. 행렬을 3*3 범위만큼 바꿔주는 함수이다. 
        - 이 연산이 아니더라도
            
            ⇒ `A[I+i][J+j] = 1-A[I+i][J+j]` 이렇게 간단하게 표현할 수 있다
            
    2. 과정 2와 같다. 행렬의 처음부터 끝까지 돌리는 과정에서 행렬A 값과 B값이 다른 위치가 있다면 행렬변환을 진행한다. `cnt`또한 1만큼 증가시켜 준다.
    3. 모든 과정이 끝난 후 
        - 행렬 A가 B로 바뀌었다면 cnt를 출력하고,
        - A와 B가 다른 부분이 있다면 -1을 출력한다.
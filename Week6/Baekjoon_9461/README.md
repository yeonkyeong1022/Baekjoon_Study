# [파도반 수열](https://www.acmicpc.net/problem/9461)

| 시간 제한 | 메모리 제한 | 난이도 |
| --- | --- | --- |
| 1 초 | 128 MB | silver 3 |

## 문제

![https://www.acmicpc.net/upload/images/pandovan.png](https://www.acmicpc.net/upload/images/pandovan.png)

오른쪽 그림과 같이 삼각형이 나선 모양으로 놓여져 있다. 첫 삼각형은 정삼각형으로 변의 길이는 1이다. 그 다음에는 다음과 같은 과정으로 정삼각형을 계속 추가한다. 나선에서 가장 긴 변의 길이를 k라 했을 때, 그 변에 길이가 k인 정삼각형을 추가한다.

파도반 수열 P(N)은 나선에 있는 정삼각형의 변의 길이이다. P(1)부터 P(10)까지 첫 10개 숫자는 1, 1, 1, 2, 2, 3, 4, 5, 7, 9이다.

N이 주어졌을 때, P(N)을 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. (1 ≤ N ≤ 100)

## 출력

각 테스트 케이스마다 P(N)을 출력한다.

## Code

```python
from sys import stdin 

T = int(input())
for i in range(T):
    n = int(stdin.readline())
    d = [0]*101 
    d[1] = 1
    d[2] = 1
    d[3] = 1
    for j in range(3, n+1):
        d[j] = d[j-2]+d[j-3]
        
    print(d[n])
```

- 보텀업 방식으로 구현했다.
- 피보나치 수열과 동일한 방식으로, 점화식만 조금 다르고 나머지는 모두 동일하다.
- 점화식: i번째 파도반 수를 f(i)라 하면
    - $f(i) = f(i-2)+f(i-3)$
    - $f(1) = f(2)=f(3) = 1$
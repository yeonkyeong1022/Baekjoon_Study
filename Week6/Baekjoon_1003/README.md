# [피보나치 함수](https://www.acmicpc.net/problem/1003)

| 시간 제한 | 메모리 제한 | 난이도 |
| --- | --- | --- |
| 0.25 초 | 128 MB | silver 3 |

## 문제

다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.

```
int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}

```

`fibonacci(3)`을 호출하면 다음과 같은 일이 일어난다.

- `fibonacci(3)`은 `fibonacci(2)`와 `fibonacci(1)` (첫 번째 호출)을 호출한다.
- `fibonacci(2)`는 `fibonacci(1)` (두 번째 호출)과 `fibonacci(0)`을 호출한다.
- 두 번째 호출한 `fibonacci(1)`은 1을 출력하고 1을 리턴한다.
- `fibonacci(0)`은 0을 출력하고, 0을 리턴한다.
- `fibonacci(2)`는 `fibonacci(1)`과 `fibonacci(0)`의 결과를 얻고, 1을 리턴한다.
- 첫 번째 호출한 `fibonacci(1)`은 1을 출력하고, 1을 리턴한다.
- `fibonacci(3)`은 `fibonacci(2)`와 `fibonacci(1)`의 결과를 얻고, 2를 리턴한다.

1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, `fibonacci(N)`을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.

## 출력

각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.

## Code

```python
from sys import stdin 
T = int(input())
for i in range(T):
    d = [ [0, 0] for i in range(41)]
    d[0][0] = 1
    d[1][1] = 1
    N = int(stdin.readline())

    for j in range(2, N+1):
        d[j][0] = d[j-1][0]+d[j-2][0]
        d[j][1] = d[j-1][1]+d[j-2][1]

    print(d[N][0], d[N][1])
```

- 보텀업 방식으로 구현했다.
- 평범한 피보나치 수열에서 f(i)는 i번째 피보나치 수이고, 이는 f(1)이 호출된 횟수와 동일하다.
- f(0)과 f(1)이 각각 몇 번 호출되었는지 저장하는 배열 d를 만든다
    - d = [[f(0)이 호출된 횟수, f(1)이 호출된 횟수]]
    - d[0]과 d[1]은 각각 [1, 0], [0, 1]로 초기화 시켜주고 시작한다.
- 일반적인 피보나치 수열의 보텀업 형식과 비슷하게, d[j]에 d[j-1]과 d[j-2]가 호출한 f(0)과 f(1)의 수를 더해주며 숫자를 높여간다.
- 마지막으로 n번째 피보나치 수열에 저장된 호출 횟수를 출력해준다.
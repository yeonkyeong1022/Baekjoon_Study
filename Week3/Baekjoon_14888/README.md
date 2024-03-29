# 연산자 끼워넣기

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 512 MB | 88107 | 40067 | 26804 | 47.788% |

## 문제

N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다. 또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다. 연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다.

우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다. 이때, 주어진 수의 순서를 바꾸면 안 된다.

예를 들어, 6개의 수로 이루어진 수열이 1, 2, 3, 4, 5, 6이고, 주어진 연산자가 덧셈(+) 2개, 뺄셈(-) 1개, 곱셈(×) 1개, 나눗셈(÷) 1개인 경우에는 총 60가지의 식을 만들 수 있다. 예를 들어, 아래와 같은 식을 만들 수 있다.

- 1+2+3-4×5÷6
- 1÷2+3+4-5×6
- 1+2÷3×4-5+6
- 1÷2×3-4+5+6

식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다. 이에 따라서, 위의 식 4개의 결과를 계산해보면 아래와 같다.

- 1+2+3-4×5÷6 = 1
- 1÷2+3+4-5×6 = 12
- 1+2÷3×4-5+6 = 5
- 1÷2×3-4+5+6 = 7

N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100) 셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다.

## 출력

첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력한다. 연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다. 또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.

---

### 풀이

```python
from sys import stdin 

N = int(stdin.readline())
AList = list(map(int, stdin.readline().split()))
operators = list(map(int, stdin.readline().split()))    
minAns = 1000000001
maxAns = -1000000001

def dfs(result, numIdx):
    global minAns, maxAns

    if numIdx>=N:               # 1
        if minAns>=result:
            minAns = result
        if maxAns<=result:
            maxAns = result
        return

    num = AList[numIdx]
    nextResult = [result+num, result-num, result*num, int(result/num)] # 2

    for i in range(4):      # 3
        if operators[i] >0:
            operators[i]-=1      # 3.a
            dfs(nextResult[i], numIdx+1)   
            operators[i]+=1      # 3.b
    
dfs(AList[0], 1)

print(maxAns)
print(minAns)
```

- **백트래킹 알고리즘을 사용한다.**
    - 함수를 재귀적으로 호출하여 모든 연산자의 조합을 구한다.
1. numIdx가 N이상이라면 모든 숫자가 연산되었다는 것이므로 최종 결과값과 최소,최대값을 비교한다.
2. 현재 결과값과 다음 피연산자와의 계산 결과 리스트
    1. 나눗셈의 경우 python과 c/c++에서 음수와 나눗셈의 결과가 다르다. 문제에서 c++14의 기준을 따른다고 명시했으므로 result//num이 아닌 int(result/num)으로 계산해야 옳다.
3. 반복문을 돌리며 남아있는 연산자의 개수만큼 연산한다.
    1. 연산자가 존재하면 한 개 감소시킨 뒤 해당 연산 결과값을 다음 함수의 인자로 넘겨준다. 인덱스도 1 증가시킨다. 끝까지 연산했으면 다시 되돌아온다.
    2. 반환한 뒤 사용했던 연산자는 다시 되돌려 놓는다(하나 감소했던 개수를 다시 늘려준다.)
# 스타트와 링크

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 512 MB | 85131 | 41796 | 24530 | 46.142% |

## 문제

오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 축구는 평일 오후에 하고 의무 참석도 아니다. 축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다. 능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다. 팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.

N=4이고, S가 아래와 같은 경우를 살펴보자.

| i\j | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| 1 |  | 1 | 2 | 3 |
| 2 | 4 |  | 5 | 6 |
| 3 | 7 | 1 |  | 2 |
| 4 | 3 | 4 | 5 |  |

예를 들어, 1, 2번이 스타트 팀, 3, 4번이 링크 팀에 속한 경우에 두 팀의 능력치는 아래와 같다.

- 스타트 팀: $S_{12}+S_{21}=1+4=5$
- 링크 팀: $S_{34}+S_{43}=2+5=7$

1, 3번이 스타트 팀, 2, 4번이 링크 팀에 속하면, 두 팀의 능력치는 아래와 같다.

- 스타트 팀:$S_{13}+S_{31}=22+7=9$
- 링크 팀: $S_{24}+S_{42}=6+4=10$

축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다. 위의 예제와 같은 경우에는 1, 4번이 스타트 팀, 2, 3번 팀이 링크 팀에 속하면 스타트 팀의 능력치는 6, 링크 팀의 능력치는 6이 되어서 차이가 0이 되고 이 값이 최소이다.

## 입력

첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다. 각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다. Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.

## 출력

첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다

---

### 풀이

```python
from sys import stdin 

N = int(stdin.readline())
array = [i for i in range(N)]
S = [] 
used = [False for i in range(N)]           # 1
minDiff = 500
for i in range(N):
    S.append(list(map(int, stdin.readline().split())))
K = N//2   # 두 그룹으로 나누어야 하므로(K만큼 뽑는 조합의 수)

def comb(idx, combLen):             # 2
    global minDiff
    if combLen == K:                           # 4
        
        startTeam = 0
        linkTeam = 0

        for i in range(N-1):
            for j in range(i+1, N):
                if used[i] == True and used[j]==True:  # 4.a
                    startTeam+=(S[i][j]+S[j][i])
                elif used[i]==False and used[j]==False:
                    linkTeam+=(S[i][j]+S[j][i])

        abilityDiff = abs(startTeam-linkTeam)          # 5
        if minDiff>abilityDiff:
            minDiff = abilityDiff
        return 
    
    for i in range(idx+1, len(array)):               # 3
        if used[i] == False:
            used[i] = True
            comb(i, combLen+1)
            used[i] = False 
    return 

comb(-1, 0)

print(minDiff)
```

- 팀을 두 그룹으로 나누어야 하므로 **조합**을 사용한다.
    - 파이썬 내부 라이브러리인 **itertools**를 사용하여 손쉽게 조합을 구할 수 있으나, **코딩테스트의 경우 금지되어있는 경우가 종종 있다고 한다.** 그렇지 않더라도 직접 구현해보는 것이 훨씬 공부가 될 것.
    - **팀을 둘로 나누는 경우를 모두 구하여 각 경우에 대해 능력치 차이를 구한다.**
1. **used[]** : start 팀은 True로, link팀은 False로 표시하는 용도이다. False로 초기화 해두고 재귀함수를 거쳐가며 start팀으로 뽑힌 팀원의 인덱스를 True로 표시해간다. 
2. **comb()** 함수 : start팀과 link 팀을 두 팀으로 나누는 조합을 구하기 위한 함수이다. 재귀적으로 호출한다.
    1. 매개변수 idx는 현재 start팀으로 선택된 팀원의 인덱스이고, combLen은 start 팀으로 선택된 팀원의 수 이다.  
3. 반복문을 돌며 start팀을 한 명씩 고른다. 고른 경우 start팀원의 수(combLen)를 하나 늘려준 채로 다음 함수로 넘겨준다. used의 [i] 번째도 True로 표시한다. 재귀함수에서 빠져나왔다면 start팀으로 골랐던 팀원을 다시 link팀으로 돌려준다.(false로 설정)
4. start 팀원 수가 절반에 다다랐다면 팀을 둘로 나누었다는 것이므로, 이 때 팀원의 능력치를 구한다.
    1. 반복문을 돌며 i와 j가 둘 다 true라면 start 팀, 둘 다 false라면 link 팀 점수로 계산해준다.
5. start, link팀원 능력치를 모두 구했다면 차이의 절댓값을 취하고 최소값과 비교해준다.

- [참고](https://jungsiroo.github.io/algorithm/2023-04-05-backtrack/)
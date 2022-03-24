# 1966_README.md

## 문제

> 여러분도 알다시피 여러분의 프린터 기기는 여러분이 인쇄하고자 하는 문서를 인쇄 명령을 받은 ‘순서대로’, 즉 먼저 요청된 것을 먼저 인쇄한다. 여러 개의 문서가 쌓인다면 Queue 자료구조에 쌓여서 FIFO - First In First Out - 에 따라 인쇄가 되게 된다. 하지만 상근이는 새로운 프린터기 내부 소프트웨어를 개발하였는데, 이 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다
> 
> 1. 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
> 2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
> 
> 예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.
> 
> 여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.
> 

---

## 입력

> 첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.
> 
> 
> 테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다. 이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다
> 

---

## 출력

> 각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.
> 

---

## Code

```python
import sys
T = int(input()) 
for i in range(T):                           
    N,M=map(int, input().split())
    txt = list(map(int, input().split()))
    ind = M
    cnt=1                                    

    while True:                       
        tmp = txt[0]                      # 1
        if txt[0]==max(txt):              # 2
            if ind==0:                    # 2-1(a)
                break
            txt.remove(txt[0])            # 2-2(b)
						cnt+=1
        else:                             # 3
            txt.remove(txt[0])            
            txt.append(tmp)
        ind = (ind+len(txt)-1)%len(txt)   # 4
    print(cnt)
```

---

## Review

0. 변수 선언 : 

- txt : 문서를 집어넣을 list
- ind : 프린트 순서를 알고싶은 문서의 인덱스 (M으로 초기화)
- cnt : ind번째 문서가 프린트되는 순서(1로 초기화)

1. tmp : 0번째 문서를 remove하고 다시 마지막에 append하기 위한 임시 저장 변수
2. 0번째 문서가 중요도가 제일 높다면 :
    1. 그 문서가 우리가 찾는 ind 번째 문서라면 ⇒ 반복문 탈출
    2. 그렇지 않다면 ⇒ remove하고 cnt를 1만큼 증가
3. 0번째 문서보다 중요도가 높은 문서가 있다면 
    
    ⇒ 해당 문서를 맨 뒤로 보냄 (remove한 뒤 다시 append)
    
4. 문서가 한 칸 씩 앞으로 밀렸으므로 ind 1씩 감소
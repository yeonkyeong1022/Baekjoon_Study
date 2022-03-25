# [최대 힙](https://www.acmicpc.net/problem/11279)

## 문제

> 널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.
> 
> 1. 배열에 자연수 x를 넣는다.
> 2. 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
> 
> 프로그램은 처음에 비어있는 배열에서 시작하게 된다.
> 

## 입력

> 첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 입력되는 자연수는 231보다 작다.
> 

## 출력

> 입력에서 0이 주어진 회수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우에는 0을 출력하면 된다.
> 

---

## Code

```python
import sys

data = [None]                          #1
N = int(input())
for i in range(N):
    x = int(sys.stdin.readline())
    if x>0:
        data.append(x)                 # 2
        l = len(data)-1                
        while l>1:                     # 2-1(a)
            if data[l]>data[l//2]: 
                data[l], data[l//2] = data[l//2], data[l]
                l=l//2
            else :
                break
    elif len(data)==1:
        print("0")
    else :                             # 3
        data[1], data[-1] = data[-1], data[1]
        print(data.pop())
        maxHeap(data, 1)

def maxHeap(arr, i):
    left = 2*i
    right = (2*i)+1
    min = i
    if left<len(arr) and data[i]<data[left]:     # a
        min = left
    if right<len(arr) and data[i]<data[right]:   # b
        min = right
        if data[right]<data[left]:               # b-1
            min = left
    if min != i:                                
        data[i], data[min] = data[min], data[i]
        maxHeap(arr, min)
```

## review

1. 최대 힙의 배열(또는 리스트) 기반 구현에서는 0번째 인덱스 사용 안하므로
2. 자연수일 경우 : 힙 배열의 가장 마지막에 새로운 데이터 삽입
    1. 새로운 노드 기준으로 부모노드와 비교 → 자식노드가 더 클 경우 자리 변경
        
        ⇒부모노드가 더 클 때 까지 반복
        
3. 데이터 추출 : 가장 마지막 노드와 첫 번째 노드(최대값 노드) 자리 변경
    
    ⇒ `maxHeap()` 함수 사용
    
    - maxHeap() : 부모노드 기준으로 자식노드와 비교
        1. 왼쪽 노드가 존재하고, 부모노드보다 크면 ⇒ 자리 변경
        2. 오른쪽 노드가 존재하고, 부모노드보다 크면 ⇒ 자리변경(elif문을 쓰지 않는다)
            
            ⇒ 만약 왼쪽노드가 더 크면 : 다시 왼쪽이랑 자리변경
            

---

## 참고

- [[파이썬 자료구조] :: 힙(Heaps)](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=leeinje66&logNo=221622360256)
- [우선순위 큐와 힙](https://www.notion.so/Chapter-09-4f293a97fd7348c19961e32860aebb20)
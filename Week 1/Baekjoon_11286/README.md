# [절댓값 힙](https://www.acmicpc.net/problem/11286)

## 문제

> 절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.
> 
> 1. 배열에 정수 x (x ≠ 0)를 넣는다.
> 2. 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
> 
> 프로그램은 처음에 비어있는 배열에서 시작하게 된다.
> 

## 입력

> 첫째 줄에 연산의 개수 N(1≤N≤100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 만약 x가 0이 아니라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 입력되는 정수는 -231 보다 크고, 231 보다 작다.
> 

## 출력

> 입력에서 0이 주어진 횟수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 절댓값이 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.
> 

---

## Code

```python
import sys
def minHeap(arr, i):
    left = 2*i
    right = (2*i)+1
    min = i
    if left<len(arr) and (abs(data[i])>abs(data[left]) or abs(data[i])==abs(data[left]) and data[i]>data[left]):
        min = left
    if right<len(arr) and (abs(data[i])>abs(data[right]) or abs(data[i])==abs(data[right]) and data[i]>data[right]):
        min = right
        if abs(data[right])>abs(data[left]) or abs(data[right])==abs(data[left]) and data[right]>data[left]:
            min = left
    if min != i:
        data[i], data[min] = data[min], data[i]
        minHeap(arr, min)
data = [None]
N = int(input())
for i in range(N):
    x = int(sys.stdin.readline())
    if x!=0:
        data.append(x)
        l = len(data)-1
        while l>1:
            if abs(data[l])<abs(data[l//2]) or abs(data[l])==abs(data[l//2]) and data[l]<data[l//2]: 
                data[l], data[l//2] = data[l//2], data[l] #교환
                l=l//2 
            else :
                break
    elif len(data)==1:
        print("0")
    else :
        data[1], data[-1] = data[-1], data[1]
        print(data.pop())
        minHeap(data, 1)
```

최대 힙에서 부등호 방향만 바꾸고 

maxHeap의 if 조건을 조금 추가했다

⇒ 자식노드 절댓값이 더 작거나 of 절댓값은 같고 값은 더 작을 경우 교환

visual studio code에서 돌리니까 list 범위를 벗어난다고 오류가 나던데 영 틀린곳을 못찾겠어서 그냥 백준에 제출해봤더니 맞다고 나왔다 띠용,,
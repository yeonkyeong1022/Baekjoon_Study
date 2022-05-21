# 이코테 강의 04.

# 정렬(Sorting)

:데이터를 특정한 기준에 따라 순서대로 나열하는 것

### 선택 정렬

: 처리되지 않은 데이터 중에서 **가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것**을 반복

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)
```

- 시간복잡도 = $O(N^2)$

### 삽입 정렬

: 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    for j in range(i, 0, -1):
        if array[j]<array[j-1]:
            array[j], array[j-1] = array[j-1],array[j]
        else:
            break 
        
print(array)
```

- 시간복잡도 = $O(N^2)$

### 퀵정렬

: **기준 데이터(Pivot)**를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꿈

```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start>=end:
        return 
    pivot = start
    left = start+1
    right = end
    while(left<=right):
        while(left<=end and array[left] <= array[pivot]):
            left +=1
        while(right>start and array[right]>=array[pivot]):
            right -= 1
        if(left>right):
            array[right],array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
        quick_sort(array, start, right-1)
        quick_sort(array, right+1, end)
quick_sort(array, 0, len(array)-1)
print(array)
```

시간 복잡도 = $O(NlogN)$

### 계수 정렬

: 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘이다

- 계수 정렬은 데이터 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능
- 시간복잡도 = $O(N+K)$ (데이터 개수 N, 데이터 최댓값 K)
1. 가장 작은 데이터부터 가장 큰 데이터까지의 범위가 모두 담길 수 있도록 리스트 생성
2. 데이터를 하나씩 확인하며 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가
3. 결과적으로 최종 리스트에는 각 데이터가 몇 번씩 등장했는지 그 횟수 기록
4. 결과를 확인할 때는 리스트의 첫 번째 데이터부터 하나씩 그 값만큼 반복하여 인덱스 출력

```python
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
```
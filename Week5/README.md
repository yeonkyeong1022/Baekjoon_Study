# 이코테 강의 05
# 이진탐색

### 탐색 종류:

- **순차탐색:** 리스트 안에 있는 특정한 **데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인**하는 방법
- **이진 탐색:**  정렬되어 있는 리스트에서 **탐색 범위를 절반씩 좁혀가며 데이터를 탐색**하는 방법
    
    ⇒ 시작점, 끝점, 중간점을 이용하여 탐색범위 설정
    

### 이진탐색의 시간복잡도

- 이진 탐색은 탐색 범위를 절반씩 줄이며, 시간복잡도는 $O(log_N)$을 보장

### 소스코드

```python
def binary_search(array, target, start, end):
    if start>end:
        return None;
    mid = (start+end)//2 
    
    if array[mid] == target:
        return mid
    elif array[mid]>target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result ==None:
    print("원소가 존재하지 않음.")
else:
    print(result + 1)
```

### bisect : 이진탐색 라이브러리

- **bisect_left(a, x):** 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스 반환
- **bisect_right(a, x):** 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스 반환

```python
from bisect import bisect_left, bisect_right 

a = [1, 2, 4, 4, 8]
x=4 

print(bisect_left(a, x))
print(bisect_right(a, x))
```

⇒ 실행결과

```python
2
4
```

## 파라메트릭 서치(Parametric Search)

:**최적화 문제를 결정 문제(’예’ 혹은 ‘아니오’)로 바꾸어 해결하는 기법이다.**

- 일반적으로 코딩테스트에서 파라메트릭 서치 문제는 이진탐색을 이용하여 해결할 수 있다.

### 문제: 떡볶이 떡 만들기

- **문제 설명:**
    - 오늘 동빈이는 여행가신 부모님을 대신해서 떡집 일을 하기로 했다. 오늘은 떡볶이 떡을 만드는 날이다. 동빈이네 떡볶이 떡은 재밌게도 떡볶이 떡의 길이가 일정하지 않다. 대신에 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다.
    - 절단기에 **높이(H)**를 지정하면 줄지어진 떡을 한 번에 절단한다. 높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
    - 예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 16cm로 지정하면 자른 뒤 떡의 높이는 15, 14, 10, 15cm 가 될 것이다. 잘린 떡의 길이는 차례대로 4, 0, 0, 2cm이다. 손님은 6cm만큼의 길이를 가져간다.
    - 손님이 왔을 때 요청한 총 길이가 M일 때 **적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램**을 작성하라.
    
- **문제 조건:**
    - **난이도 : ★★☆ | 풀이 시간 40분 | 시간제한 2초 | 메모리 제한 128MB**
    - **입력 조건:**
        - 첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다(1≤N≤1,000,000, 1≤M≤2,000,000,000)
        - 둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M이상이므로, 손님은 필요한 양만큼 떡을 사갈 수 있다. 높이는 10억보다 작거나 같은 양의 정수 또는 0이다.
    - **출력 조건:**
        - 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.
    - 입력 예시
        
        ```python
        4 6
        19 15 10 17
        ```
        
    - 출력 예시
        
        ```python
        15
        ```
        

- **문제 풀이:**
    - 적절한 높이를 찾을 때까지 이진 탐색을 수행하여 높이 H를 반복해서 조정해준다.
    - ‘현재 이 높이로 자르면 조건을 만족할 수 있는가?’를 확인한 뒤에 **조건의 만족 여부(’예’ 혹은 ‘아니오’)에 따라서 탐색 범위를 좁혀서 해결**할 수 있다.
    - 절단기 높이는 0부터 10억까지의 정수 중 하나이다.
        - 이렇게 범위가 클 경우 **이진탐색**을 먼저 떠올려야 한다.
    - 중간접의 값은 **시간이 지날수록 ‘최적화된 값’**이 되므로, 과정을 반복하면서 얻을 수 있는 떡의 길이 합이 필요한 떡의 길이보다 크거나 같을 때마다 중간점의 값을 기록한다.
- **답안 코드:**
    
    ```python
    n, m = list(map(int, input().split(' ')))
    
    array = list(map(int, input().split()))
    
    start = 0
    end = max(array) 
    
    result = 0
    while(start<=end):
        total = 0 
        mid = (start+end)//2
        for x in array:
            if x>mid:
                total += x-mid 
        
        if total<m:
            end = mid-1 
        else:
            result = mid 
            start = mid + 1
    print(result)
    ```
    

### 문제: 정렬된 배열에서 특정 수의 개수 구하기:

- **문제 설명:**
    - N개의 원소를 포함하고있는 수열이 오름차순으로 정렬되어 있다. 이 때 이 수**열에서 x가 등장하는 횟수를 계산**하시오. 예를 들어 수열 {1, 1, 2, 2, 2, 2, 3} 이 있을 때 x=2라면, 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력한다.
    - 단, 이 문제는 시간 복잡도 $O(logN)$으로 알고리즘을 설계하지 않으면 **시간 초과** 판정을 받는다.
- **문제 조건:**
    - **난이도 : ★★☆ | 풀이 시간 30분 | 시간제한 1초 | 메모리 제한 128MB**
    - **입력 조건:**
        - 첫째 줄에 N과 x가 정수 형태로 공백으로 구분되어 입력된다.(1 ≤ N ≤ 1,000,000), (-10^8 ≤ x ≤ 10^9)
        - 둘째 줄에 N개의 원수가 정수 형태로 공백으로 구분되어 입력된다.
    - **출력 조건:**
        - 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.
- 입력 예시
    
    ```python
    7 2
    1 1 2 2 2 2 3
    ```
    
- 출력 예시
    
    ```python
    4
    ```
    
- **문제 풀이 :**
    - 시간 복잡도 $O(logN)$으로 동작하는 알고리즘을 요구하고 있다.
        - 일반적인 **선형 탐색(Linear Search)로는 시간 초과 판정**을 받는다.
        - 하지만 데이터가 정렬되어있기 때문에 **이진 탐색을 수행**할 수 있다.
    - 특정 값이 등장하는 첫 번째 위치와 마지막 위치를 찾아 위치 차이를 계산해 내는 문제를 해결할 수 있다.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cee261f5-8dfc-4a12-be79-2ae0702564c0/Untitled.png)
    
- **답안 코드:**
    
    ```python
    from bisect import bisect_left, bisect_right 
    
    def count_by_range(array, left_value, right_value):
        right_index = bisect_right(array, right_value)
        left_index = bisect_left(array, left_value)
        return right_index - left_index
    
    n, x = map(int, input().split())
    array = list(map(int, input().split()))
    
    count = count_by_range(array, x, x)
    
    if count == 0:
        print(-1)
    
    else:
        print(count)
    ```
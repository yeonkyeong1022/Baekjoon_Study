# 이코테 강의 08 : 기타 그래프 이론

# 서로소 집합(Disjoint Sets)

: 공통 원소가 없는 두 집합

- 서로소 관계인지 아닌지 판단하는 경우, 원소를 확인하여 판단한다.
    
    ![Alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/80df67be-21a6-48d5-8f39-051cace89720/Untitled.png)
    
    - 원소 1과 2를 가지는 집합과 원소 3, 4를 가지는 집합은 겹치는 원소가 없어 서로소 관계이다.

## 서로소 집합 자료구조

- **서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조**
- 서로소 집합 자료구조는 두 종류의 연산을 지원한다.
    - **합집합(Union)** : 두 개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
        - 합집합 연산을 수행할 때 두 원소에 대해 연산을 진행하는데, 이 때 두 원소의 각 집합이 같은 집합이 될 수 있도록 합쳐준다.
    - **찾기(Find) :** 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산
        - 예를들어, 두 개의 원소가 주어졌을 때, 두 원소가 같은 집합에 포함되어있는지 확인해주는 연산이다.
- 서로소 집합 자료구조는 **Union-Find 자료구조** 라고 불리기도 한다.
- 여러 개의 합치기 연산이 주어졌을 때 서로소 집합 자료구조의 동작 과정은 다음과 같다.
    1. 합집합(Union) 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인한다.
        1. A와 B의 루트 노드 A’, B’를 각각 찾는다
        2. A’를 B’의 부모 노드로 설정한다.
    2. 모든 합집합(Union) 연산을 처리할 때 까지 1번의 과정을 반복한다.

### 동작과정 예시

- **처리할 연산들** : `Union(1, 4)`, `Union(2, 3)`, `Union(2, 4)`, `Union(5, 6)`
- **[초기 단계]** 노드의 개수 크기만큼의 부모 테이블을 초기화 한다.
    
    ![Alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a3a45b13-a2eb-40d2-837a-2dbe34ce60b7/Untitled.png)
    
    - 처음에는 부모를 모두 자기 자신으로 설정한다.
    - 6개의 집합은 모두 서로 다른 집합으로 구분된다.
- **[Step 1]** 노드 1과 노드 4의 루트 노드를 각각 찾는다. 현재 루트 노드는 각각 1과 4이므로 더 큰 번호에 해당하는 루트 노드 4의 부모를 1로 설정한다.
    
    ![Alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5833f491-3a0d-430b-8545-25f72b488ba7/Untitled.png)
    
- ****************[Step 2]**************** 노드 2와 노드 3의 루트 노드를 각각 찾는다. 현재 루트 노드는 각각 2와 3이므로 더 큰 번호에 해당하는 루트 노드 3의 부모를 2로 설정한다.
    
    ![Alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f461cbd9-0202-40e3-bd3b-5468d19ed5fb/Untitled.png)
    
- ****************[Step 3]**************** 노드 2와 노드 4의 루트 노드를 각각 찾는다. 현재 루트 노드는 각각 2와 1이므로 더 큰 번호에 해당하는 루트 노드 2의 부모를 1로 설정한다.
    
    ![Alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/44228494-bcde-43a8-b454-0f749de6954d/Untitled.png)
    
- ****************[Step 4]**************** 노드 5와 노드 6의 루트 노드를 각각 찾는다. 현재 루트 노드는 각각 5와 6이므로 더 큰 번호에 해당하는 루트 노드 6의 부모를 5로 설정한다.
    
    ![Alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/51b4619f-3e85-439b-a4ef-cee29f41f123/Untitled.png)
    

### 연결성

- 서로소 집합 자료구조에서는 연결성을 통해 손쉽게 집합의 형태를 확인할 수 있다.
    
    ![Alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/44089b5e-eac3-47be-8e81-57d492b23104/Untitled.png)
    
- 기본적인 형태의 서로소 집합 자료구조에서는 루트 노드에 즉시 접근할 수 없다.
    - 루트 노드를 찾기 위해 **부모 테이블을 계속해서 확인**하며 재귀적으로 거슬러 올라가야 한다.
- 다음 예시에서 노드 3의 루트를 찾기 위해서는 노드 2를 거쳐 노드 1에 접근해야 한다.
    
    ![Alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d662b01e-7c6c-4cb6-9677-60414c3a8485/Untitled.png)
    

### 기본적인 구현방법

```python
# 특정 원소가 속한 집합을 찾기 (Find)
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x 

# 두 원소가 속한 집합을 합치기 (Union)
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a 
    else:
        parent[a] = b 
    
# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent=[0] *(v+1) # 부모 테이블 초기화

# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i 

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합: ', end = '')
for i in range(1, v+1):
    print(find_parent(parent, i), end= ' ')

print() 

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')
```

### 기본적인 구현 방법의 문제점

- 합집합(Union) 연산이 편향되게 이루어지는 경우 찾기(Find) 함수가 비효율적으로 동작한다.
    - 현재 노드에서 부모테이블을 참조하여 부모를 다시 재귀적으로 참조하는 과정을 반복한다.
- 최악의 경우에는 찾기(Find)함수가 모든 노드를 다 확인하게 되어 시간 복잡도가 O(V) 이다.
    - 다음과 같이 {1, 2, 3, 4, 5}의 총 5개의 원소가 존재하는 상황의 경우
    - 수행된 연산들: `Union(4, 5)`, `Union(3, 4)`, `Union(2, 3)`, `Union(1, 2)`
    
    ![Alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2975c410-c694-4a58-8caa-e4f8fd25cc35/Untitled.png)
    
    - 이 때 5번 노드에서 Find 연산을 수행하면 4, 3, 2, 1번 노드를 모두 확인하게 된다.

## 해결책 : 경로 압축

- 찾기(Find) 함수를 최적화 하기 위한 방법으로 경로 압축(Path Compression)을 이용할 수 있다.
    - 찾기(Find) 함수를 재귀적으로 호출한 뒤 **부모 테이블 값을 바로 갱신**한다.
    
    ```python
    # 특정 원소가 속한 집합을 찾기
    def find_parent(parent, x):
        # 루트 노드가 아니라면, 로트 노드를 찾을 때 까지 재귀적으로 호출
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]
    ```
    
    - 루트노드를 찾을 때 까지 재귀적으로 호출한 뒤 그 반환값을 자신의 부모값이 되도록 대입한다.
    - 이전까지는 같은 집합이더라도 부모 노드가 다른 노드 값일 수 있었지만, 새 Find 함수에서는 같은 집합이면 부모 노드는 항상 같은 루트 노드를 가지도록 한다.
- 경로 압축 기법을 적용하면 각 노드에 대하여 **찾기(Find) 함수를 호출한 이후**에 해당 노드의 루트 노드가 바로 부모 노드가 된다.
- 동일한 예시에서 **모든 합집합(Union) 함수를 처리한 후 각 원소에 대하여 찾기(Find) 함수를 수행하면 다음과 같이 부모 테이블이 갱신**된다.
- 기본적인 방법에 비하여 시간 복잡도가 개선된다.

![Alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fbf6514d-c40a-4ae4-a1a5-7fbfa418a728/Untitled.png)

## 서로소 집합을 활용한 사이클 판별

- 서로소 집합은 **무방향 그래프 내에서의 사이클을 판별**할 때 사용할 수 있다.
    - 참고로 방향 그래프에서의 사이클 여부는 DFS를 이용하여 판별할 수 있다.
- **사이클 판별 알고리즘**은 다음과 같다.
    1. 각 간선을 하나씩 확인하며 두 노드의 루트 노드를 확인한다.(Find 연산 수행)
        1. 루트 노드가 서로 다르다면 두 노드에 대하여 합집합(Union)연산을 수행한다.
        2. 루트 노드가 서로 같다면(이미 같은 집합이라면) 사이클(Cycle)이 발생한 것이다.
    2. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 반복한다.

### 동작 과정 예시

- **[초기 단계]** 모든 노드에 대하여 자기 자신을 부모로 설정하는 형태로 부모 테이블을 초기화 한다.
    
    ![Alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3b02378b-77bd-4735-bd9b-38e5bc1d5292/Untitled.png)
    
- **[Step 1]** 간선 (1, 2)를 확인한다. 노드 1과 노드 2의 루트 노드는 각각 1과 2이다. 따라서 더 큰 번호에 해당하는 노드 2의 부모노드를 1로 변경한다.
    
    ![Alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5113ce7e-d0dc-491b-82e3-fce3f1025c88/Untitled.png)
    
- **[Step 2]** 간선 (1, 3)를 확인한다. 노드 1과 노드 3의 루트 노드는 각각 1과 3이다. 따라서 더 큰 번호에 해당하는 노드 3의 부모노드를 1로 변경한다.
    - 현재 각 노드가 모두 같은 집합에 속하는 원소임을 알 수 있다.
    
    ![Alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f7e84b0f-f58b-454c-9bb2-18246b27e06d/Untitled.png)
    
- **[Step 3]** 간선 (2, 3)을 확인한다. 이미 노드 2와 노드 3의 루트 노드는 모두 1이다. 다시말해 **사이클이 발생**한다는 것을 알 수 있다.
    - 간선 정보를 확인했을 때 같은 집합에 속해있다면, 이 간선으로 인해 현재 그래프에 사이클이 발생했음을 알 수 있다.
    - 간선을 하나씩 확인하며 합치기 연산을 수행하는 것 만으로도 사이클이 발생하는지 확인하는 것이 가능하다.
    
    ![Alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b3dc4a9d-ff0c-42c9-8c95-2c3274567ce6/Untitled.png)
    
- 사이클 판별 코드
    
    ```python
    # 특정 원소가 속한 집합을 찾기
    def find_parent(parent, x):
        # 생략
        return 
    
    # 두 원소가 속한 집합을 합치기
    def union_parent(parent, a, b):
        # 생략
        return 
    
    # 노드의 개수와 간선(Union 연산)의 개수 입력 받기
    v, e = map(int, input().split())
    parent = [0]*(v+1)
    
    # 부모 테이블 상에서 부모를 자기자신으로 초기화
    for i in range(1, v+1):
        parent[i] = i 
    
    cycle = False # 사이클 발생 여부
    
    for i in range(e):
        a, b = map(int, input().split())
        # 사이클이 발생한 경우 종료
        if find_parent(parent, a) == find_parent(parent, b):
            cycle = True 
            break 
        
        # 사이클이 발생하지 않았다면 합집합(Union)연산 수행
        else:
            union_parent(parent, a, b)
    
    if cycle:
        print("사이클이 발생했습니다.")
    else:
        print("사이클이 발생하지 않았습니다.")
    ```
    

# 신장 트리

- **그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프**를 의미한다.
    - 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건은 **트리**의 조건이기도 하다.
        
        

![Alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/91a8713b-30ad-41ae-b956-556f3f2afd12/Untitled.png)

## 최소 신장 트리

: 최소한의 비용으로 구성되는 신장 트리를 찾아야 하는 경우

- 예시 : N개의 도시가 존재하는 상황에서 두 도시 사이에 도로를 놓아 전체 도시가 서로 연결될 수 있게 도로를 설치하는 경우
    - 두 도시 A, B를 선택했을 때 A에서 B로 이동하는 경로가 반드시 존재하도록 도로를 설치한다.
    - **모든 노드가 연결되어 이동 가능하도록 만들되, 최소한의 비용으로 전체 신장트리를 구하고자 하는 것이다.**
    
    ![Alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9cf2b825-da36-4963-9922-c661b4087205/Untitled.png)
    
    - 1, 3을 연결하는 간선을 제외하게 되면, 모든 노드가 연결되어있으면서 비용이 최소가 되는 신장트리가 만들어진다.

## 크루스칼 알고리즘

- 대표적인 최소 신장 트리 알고리즘으로, 그리디 알고리즘으로도 분류된다.
- 구체적인 동작 과정
    1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
    2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
        1. 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다.
        2. 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.
    3. 모든 간선에 대하여 2번의 과정을 반복한다.

### 동작 과정 예시

- **************************[초기 단계]************************** 그래프의 모든 간선 정보에 대하여 **오름차순 정렬**을 수행한다.
    
    ![Alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d4020a14-ca34-41c7-92d1-2187e36775cf/Untitled.png)
    
- **[최종 결과]** 비용이 작은 것부터 오름차순으로 선택하여 최소 신장트리에 포함시키는데, 이 과정에서 6-7을 잇는 간선과 2-3을 잇는 간선, 1-5를 잇는 간선은 사이클이 발생하여 신장트리에서 제외시킨다.
    
    ![Alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3d17d5ff-b9d5-4445-929b-7a4785be92a1/Untitled.png)
    
- 동작 코드
    
    ```python
    # 특정 원소가 속한 집합을 찾기
    def find_parent(parent, x):
        # 생략
        return 
    
    # 두 원소가 속한 집합을 합치기
    def union_parent(parent, a, b):
        # 생략
        return 
    
    # 노드의 개수와 간선(Union 연산)의 개수 입력 받기
    v, e = map(int, input().split())
    parent = [0]*(v+1)
    
    # 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
    edges = [] 
    result = 0 
    
    # 부모 테이블상에서, 부모를 자기 자신으로 초기화
    for i in range(1, v+1):
        parent[i] = i
    
    # 모든 간선에 대한 정보를 입력 받기
    for _ in range(e):
        a, b, cost = map(int, input().split())
        # 비용 순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
        edges.append((cost, a, b))
    
    edges.sort()
    
    # 간선을 하나씩 확인하며
    
    for edge in edges:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
            
    print(result)
    ```
    

### 크루스칼 알고리즘 성능

- 크루스칼 알고리즘은 간선의 개수가 E일 때, **O(ElogE)**의 시간 복잡도를 가진다.
- 크루스칼 알고리즘에서 가장 많은 시간을 요구하는 곳은 **간선 정렬을 수행**하는 부분이다.
    - 표준 라이브러리를 이용해 E 개의 데이터를 정렬하기 위한 시간 복잡도는 O(ElogE) 이다.

# 위상 정렬

- 사이클이 없는 방향그래프(DAG)의 모든 노드를 **방향성에 거스르지 않도록 순서대로 나열**하는 것을 의미한다.
- 예시 : 선수 과목을 고려한 학습 순서 설정

![Alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0ee7b294-a9cf-406d-abfe-8edf8e6d85d8/Untitled.png)

- 위 세 과목을 모두 듣기 위한 적절한 학습 순서는?
    - **자료구조 → 알고리즘 → 고급 알고리즘 (O)**
    - 자료구조 → 고급 알고리즘 → 알고리즘 (X)

## 진입 차수와 진출 차수

- 진입 차수(Indegree) : 특정한 노드로 들어오는 간선의 개수
- 진출 차수(Outdegree) : 특정한 노드에서 나가는 간선의 개수

![Alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/59e7ddba-ad11-4620-a10f-3af69da0ea8b/Untitled.png)

## 위상 정렬 알고리즘

- **큐**를 이용하는 **위상 정렬 알고리즘의 동작 과정**은 다음과 같다
    1. 진입 차수가 0인 모든 노드를 큐에 넣는다.
    2. 큐가 빌 때 까지 다음의 과정을 반복한다.
        1. 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거한다.
        2. 새롭게 진입 차수가 0이 된 노드를 큐에 넣는다.

**⇒ 결과적으로 각 노드가 큐에 들어온 순서가 위상 정렬을 수행한 결과와 같다.** 

### 동작 예시

- 위상 정렬을 수행할 사이클이 없는 방향 그래프(DAG) 준비
- ****************************[초기 단계]**************************** 초기 단계에서는 **진입 차수가 0인 모든 노드**를 큐에 넣는다.
    - 처음에 **노드 1**이 큐에 삽입된다.
    
    ![Alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8ff5a134-1a48-44e6-a248-f825e69be891/Untitled.png)
    
- [****************Step 1]**************** 큐에서 **노드 1**을 꺼낸 뒤에 **노드 1**에서 나가는 간선을 제거한다.
    - 새롭게 **진입차수가 0이 된 노**드들을 큐에 삽입한다.
    
    ![Alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4b39e6d1-7ce1-483a-81ba-49b3a5a283b5/Untitled.png)
    
- 큐에서 꺼낸 노드에서 나가는 간선을 제거하고 새롭게 진입 차수가 0이 돈 노드를 큐에 삽입 하는 과정을 반복한다.
- **위상 정렬 결과 :**
    - 큐에 삽입된 전체 노드 순서 : **1 → 2→ 5 → 3 → 6 → 4 → 7**

### 위상 정렬 특징

- 위상 정렬은 **DAG**에 대해서만 수행할 수 있다.
- 위상 정렬에서는 **여러 가지 답이 존재**할 수 있다.
    - 한 단계에서 큐에 새롭게 들어가는 원소가 2개 이상인 경우가 있다면 여러 가지 답이 존재한다.
- **모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재**한다고 판단할 수 있다.
    - 사이클에 포함된 원소 중에서 어떠한 원소도 큐에 들어가지 못한다.
- 스택을 활용한 DFS를 이용해 위상 정렬을 수행할 수도 있다.
- 위상 정렬 동작 코드
    
    ```python
    from collections import deque 
    
    # 노드의 개수와 간선의 개수를 입력 받기
    v, e = map(int, input().split())
    # 모든 노드에 대한 진입 차수는 0으로 초기화
    indegree = [0] * (v+1)
    # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
    graph = [[] for i in range(v+1)]
    
    # 방향 그래프의 모든 간선 정보를 입력 받기
    for _ in range(e):
        a, b = map(int, input().split)()
        graph[a].append(b) # 정점 A 에서 B로 이동 가능
        # 진입 차수를 1 증가
        indegree[b] += 1
    
    # 위상 정렬 함수
    def topology_sort():
        result = [] # 알고리즘 수행 결과를 담을 리스트
        q = deque() # 큐 기능을 위한 deque 라이브러리 사용
        # 처음 시작할 때는 진입 차수가 0인 노드를 큐에 삽입
        for i in range(1, v+1):
            q.append(i)
    
        # 큐가 빌 때 까지 반복
        while q:
            # 큐에서 원소 꺼내기
            now = q.popleft()
            result.append(now)
            # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
            for i in graph[now]:
                indegree[i] -= 1
                # 새롭게 진입 차수가 0이 되는 노드를 큐에 삽입
                if indegree[i] == 0:
                    q.append(i)
        # 위상 정렬 수행 결과 출력
        for i in result:
            print(i, end = ' ')
    
    topoloty_sort()
    ```
    

### 성능 분석

- 위상 정렬을 위해 차례대로 모든 노드를 확인하며 각 노드에서 나가는 간선을 차례대로 제거해야 한다.
    - 시간 복잡도 : **O(V+E)**
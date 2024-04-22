## DFS

### 표현방법

1. 인접행렬: 2차원 배열로 그래프의 연결 관계를 표현하는 방식
    - 마치 표처럼!
    - 연결되어 있지않은 노드끼리는 무한의 값(99999999)을 가지고 있다고 작성함
    - 모든 관계를 저장하므로, 노드 개수가 많을수록 메모리 낭비
<p align="center">
  <img src="https://github.com/thoongee/algorithm-python/assets/94193480/c8a08d48-3396-440c-8cc1-c309b40c05fc" alt="Image 1" width="400"/>
  <img src="https://github.com/thoongee/algorithm-python/assets/94193480/e8bd33db-82c9-4534-94d1-2d4a065864b8" alt="Image 2" width="200"/>
</p>
        
2. 인접 리스트 : 리스트로 그래프의 연결관계를 표현하는 방식
    - 각 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장
    - 연결된 정보만 저장하기 때문에 메모리 효율성 높음.
    - 연결된 정보를 하나씩 확인 → 특정 두 노드가 연결되어있는지에 대한 정보를 얻는 속도가 느림
    - 특정한 노드와 연결된 **모든 인접 노드를 순회해야 하는 경우**, 인접 리스트 방식이 인접 행렬 방식에 비해 메모리 공간의 낭비가 적다.
<p align="center">
	<img src="https://github.com/thoongee/algorithm-python/assets/94193480/1f7b1993-79b3-4d18-934c-50d402fdc3eb" alt="Image 1" width="300"/>
  	<img src="https://github.com/thoongee/algorithm-python/assets/94193480/9fae4c9b-fb61-4c7d-98ab-49e690d738f0" alt="Image 2" width="300"/>
</p>

### 특징

- like stack
    - `list.append(x)`, `list.pop()`
- 구현시, 재귀 방법 이용 ( 재귀 함수는 내부적으로 스택 자료구조와 동일 )
- 탐색 시간 복잡도: O(n)

### 동작 과정
1. 탐색 시작 노드를 스택에 삽입하고 방문처리
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
3. 2번 과정을 더 이상 수행할 수 없을 때까지 반복
	
 ### 예시 코드

```python
def dfs(graph, v, visited):
# 현재 노드(v) 방문처리
  visited[v] = True
  print(v, end='')
# 현재 노드(v)와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)

# 인접 리스트 표현 형식 :
# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)# ex) 1번 노드는 2,3,8번 노드와 연결되어 있음
# 0번 노드는 없으니까 비워둠.
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8],
         [1, 7]]

#각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False] * 9

#정의된 DFS 함수 호출
dfs(graph, 1, visited)
```

## BFS

### 표현 방법

1. 인접행렬: 2차원 배열로 그래프의 연결 관계를 표현하는 방식
    - 마치 표처럼!
    - 연결되어 있지않은 노드끼리는 무한의 값(99999999)을 가지고 있다고 작성함
    - 모든 관계를 저장하므로, 노드 개수가 많을수록 메모리 낭비
2. 인접 리스트 : 리스트로 그래프의 연결관계를 표현하는 방식
    - 각 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장
    - 연결된 정보만 저장하기 때문에 메모리 효율성 높음.
    - 연결된 정보를 하나씩 확인 → 특정 두 노드가 연결되어있는지에 대한 정보를 얻는 속도가 느림

### 특징

- like queue
- 구현 시, deque library 사용
- 탐색 시간 복잡도: O(n)
- 보통 DFS보다 BFS 구현이 조금 더 빠르다

### 알고리즘

1. 탐색 시작 노드를 queue에 삽입하고 방문 처리 한다
    1. `queue.append(x)`
2. queue에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 queue에 삽입한다
    1. `queue.popleft()`
3. 2번을 더이상 하지 못할때까지 반복한다

### 예시 코드

```python
from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
# 현재 노드(start) 방문 처리
  visited[start] = True
# queue가 빌때까지 반복
	while queue:
		# 하나의 원소를 뽑아 출력
    v = queue.popleft()
    print(v,end=' ')
		# 해당 원소와 연결된, 아직 방문하지 않은 원소들을 queue에 삽입
		for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(=DFS)# ex) 1번 노드는 2,3,8번 노드와 연결되어 있음
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8],
         [1, 7]]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (=DFS)
visited=[False]*9

bfs(graph,1,visited)
```

### 팁

- 2차원 배열의 '탐색 문제'는 그래프 형태로 바꿔서 풀면 풀이가 쉽다

<p align="center"><img src="https://github.com/thoongee/algorithm-python/assets/94193480/ac7d4d27-47e0-4714-bb3b-5222d4b627c5" width="30%">

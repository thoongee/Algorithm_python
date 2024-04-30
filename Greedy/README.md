### 개념

**"현재 상황에서 지금 당장 좋은 것만 고르는 방법"**

- **정렬, 최단 경로** 문제에서 기본 지식으로 사용됨
- **Dijkstra Algorithm** 또한 greedy algorithm으로 분류됨

### 예제

- 거스름돈 (거슬러 줘야 할 최소 동전 개수 구하기)
    - 그리디 알고리즘이 정당한 이유 : 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문
        - ex) 500원, 100원, 50원
    - (화폐의 단위가 무작위로 주어진 문제는 다이나믹 프로그래밍으로 해결할 수 있다)

### 코드 : **Dijkstra Algorithm**

- 그래프에서 한 정점에서 다른 모든 정점으로 가는 최단 경로를 찾는 알고리즘
- 이 알고리즘은 주로 가중치가 있는 그래프에서 사용됨 (가중치≠음수)

작동 방식

1. 시작 정점의 최단 경로 비용을 0으로 설정하고, 다른 모든 정점의 비용은 무한대로 설정합니다.
2. 모든 정점이 처리될 때까지 다음을 반복합니다:
    - 처리되지 않은 정점 중에서 최단 경로 비용이 가장 작은 정점을 선택합니다.
    - 이 정점을 통해 갈 수 있는 인접한 정점들의 경로 비용을 갱신합니다.

```python
import heapq

def dijkstra(graph, start):
    # 그래프의 각 정점에 대한 최단 경로 비용을 무한대로 초기화
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0  # 시작 정점의 비용은 0으로 설정
    priority_queue = [(0, start)]  # 우선순위 큐, (비용, 정점) 형태로 저장

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # 더 작은 비용의 경로가 있을 경우 무시
        if current_distance > distances[current_vertex]:
            continue

        # 인접한 정점들을 검사하며 거리 업데이트
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # 현재 저장된 거리보다 작은 거리를 찾았다면 업데이트하고 큐에 추가
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# 그래프 예시
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# 알고리즘 실행과 결과 출력
start_vertex = 'A'
distances = dijkstra(graph, start_vertex)
print(f"Starting from vertex '{start_vertex}':")
for vertex in distances:
    print(f"Distance to vertex {vertex} is {distances[vertex]}")
    
# Starting from vertex 'A':
# Distance to vertex A is 0
# Distance to vertex B is 1
# Distance to vertex C is 3
# Distance to vertex D is 4
```

### 팁

- 문제의 유형이 다양해서 암기로는 풀기 힘들다 → 많은 유형의 문제를 접해보고 풀어보는 훈련 필요
    - 문제 유형을 파악하기 어렵다면 그리디 알고리즘을 의심하고, 문제를 해결할 수 있는 탐욕적인 해결법이 존재하는지 고민해보자.
    - 그리디 알고리즘으로 해결 방법을 찾을 수 없다면,  다이나믹 프로그래밍이나 그래프 알고리즘 등으로 문제를 해결할 수 있는지를 재차 고민
- 그리디 알고리즘은 기준에 따라 좋은 것을 선택하는 알고리즘이므로 문제에서 ‘가장 큰 순서대로’, ‘가장 작은 순서대로’와 같은 기준을 알게 모르게 제시해준다
    - 대체로 이 ‘기준’은 정렬 알고리즘을 사용했을 때 만족 시킬 수 있으므로 그리디 알고리즘 문제는 **자주 정렬 알고리즘과 짝을 이뤄 출제된다**
- "문제풀이를 위한 최소한의 아이디어를 떠올리고, 이것이 정당한지 검토하기"

참고자료 : 

https://yozm.wishket.com/magazine/detail/2478/?utm_source=stibee&utm_medium=email&utm_campaign=newsletter_yozm&utm_content=contents

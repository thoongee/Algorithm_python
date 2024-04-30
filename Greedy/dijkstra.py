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
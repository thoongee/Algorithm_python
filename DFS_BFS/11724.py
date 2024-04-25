import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
# 그래프를 인접 리스트 방식으로 초기화
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

# 간선 정보 입력 받기
for _ in range(m):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start_node, visited):
    queue = deque([start_node])
    visited[start_node] = True
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return True

cnt = 0 
for i in range(1, n + 1):  # 1부터 n까지 반복
    if not visited[i]:
        if bfs(i, visited):
            cnt += 1

print(cnt)

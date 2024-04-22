import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().rstrip().split())

# 그래프를 인접 리스트 방식으로 초기화
graph = [[] for _ in range(n + 1)]

# 간선 정보 입력 받기
for _ in range(m):
    index, value = map(int, input().rstrip().split())
    graph[index].append(value)  # index에서 value로 가는 간선
    graph[value].append(index)  # value에서 index로 가는 간선 (양방향)

# 모든 노드의 인접 리스트 정렬
for sublist in graph:
    sublist.sort()

def dfs(x, visited):
    visited[x] = True
    dfs_res.append(x)
    for v in graph[x]:
        if not visited[v]:
            dfs(v, visited)

def bfs(x, visited):
    queue = deque([x])
    visited[x] = True
    bfs_res.append(x)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                bfs_res.append(i)
                queue.append(i)

# 방문 여부를 확인할 리스트
dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)

# 결과를 저장할 리스트
dfs_res = []
bfs_res = []

# 깊이 우선 탐색 실행
dfs(v, dfs_visited)
# 너비 우선 탐색 실행
bfs(v, bfs_visited)

# 결과 출력
print(' '.join(map(str, dfs_res)))
print(' '.join(map(str, bfs_res)))
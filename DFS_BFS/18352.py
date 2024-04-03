import sys
from collections import deque
input = sys.stdin.readline

n,m,k,x = map(int,input().strip().split(' '))

graph = [[] for _ in range(n+1)] # 이중 리스트 초기화 
for i in range(m):
    node, road = map(int,input().strip().split(' '))
    graph[node].append(road)

distance = [-1]*(n+1)
distance[x] = 0

queue = deque()
queue.append(x)
while queue:
    i = queue.popleft()
    for v in graph[i]:
        if distance[v] == -1:  # 아직 방문하지 않은 노드에 대해서만 처리
            distance[v] = distance[i] + 1
            queue.append(v)  # 방문하지 않은 노드만 큐에 추가


# 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력
indexes_of_k = [i for i, value in enumerate(distance) if value == k]
indexes_of_k.sort()

if len(indexes_of_k)==0:
    print(-1)
else:
    for i in range(len(indexes_of_k)):
        print(indexes_of_k[i])
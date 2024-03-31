import sys

n,m,k,x = map(int,input().strip().split(' '))

graph = [[] for _ in range(n+1)] # **이중 리스트 초기화**
for i in range(m):
    node, road = map(int,input().strip().split(' '))
    graph[node].append(road)

cities = [1000000]*(n+1) # m의 최대값이 1000000이라서.
cities[0] = 0
cities[x] = 0  # 0번째와 x번째 노드는 거리가 0

def dfs(graph, v):
# 현재 노드(v)와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        new_cities = cities[v]+1
        cities[i] = min(new_cities,cities[i])
        dfs(graph, i)

#정의된 DFS 함수 호출
dfs(graph, x)

# 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력
indexes_of_k = [i for i, value in enumerate(cities) if value == k]
indexes_of_k.sort()

if len(indexes_of_k)==0:
    print(-1)
else:
    for i in range(len(indexes_of_k)):
        print(indexes_of_k[i])
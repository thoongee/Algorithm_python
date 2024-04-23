import sys
input = sys.stdin.readline


n = int(input().strip())

graph = []
for i in range(n):
    graph.append(list(map(int, input().strip())))

visited = [[False] * n for _ in range(n)]

# 각 단지별 집의 수를 저장할 딕셔너리
home_count = {}

def dfs(x, y, cnt):
    if x < 0 or y < 0 or x >= n or y >= n:
        return
    if graph[x][y] == 1 and not visited[x][y]:
        visited[x][y] = True
        graph[x][y] = cnt
        if cnt not in home_count:
            home_count[cnt] = 1
        else:
            home_count[cnt] += 1

        # 상하좌우 탐색
        dfs(x-1, y, cnt)
        dfs(x+1, y, cnt)
        dfs(x, y-1, cnt)
        dfs(x, y+1, cnt)

cnt = 2  # 단지 번호는 2부터 시작(1은 집이 있는 위치를 나타내므로)
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            dfs(i, j, cnt)
            cnt += 1

print(cnt - 2)  # 단지 번호가 2부터 시작했으므로 총 단지수는 cnt - 2

# 단지별 집의 수를 오름차순으로 정렬하여 출력
for count in sorted(home_count.values()):
    print(count)

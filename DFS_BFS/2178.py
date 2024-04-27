# (1,1)에서 출발, (n,m) 도착
# 도착지점까지 갈 수 있는 최소 칸의 수 구하기
# 1이라고 적힌 칸만 이동 가능
# (1,1) 지점에서부터 BFS를 수행하여 모든 노드의 값을 거리 정보로 넣으면 됨.

from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().strip().split()) # 공백으로 구분하여 입력받기

graph=[]

for i in range(n):
    graph.append(list(map(int,input().strip())))

#이동할 방향(상,하,좌,우)
dx = [-1,1,0,0] 
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque([(x,y)])

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            #미로 공간을 벗어난 경우
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            #이동할 수 없는 칸(==0)인 경우
            if graph[nx][ny] == 0:
                continue
            #해당 노드를 처음 방문하는 경우 
            if graph[nx][ny]==1:
                # 최단 거리 기록(해당 노드의 값을 이동한 칸 개수로 표시)
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    #최단 거리 반환
    return graph[n-1][m-1]


print(bfs(0,0)) # 문제에서는 (1,1)에서 시작한다고 하였으나, 인덱스는 (0,0)부터 시작

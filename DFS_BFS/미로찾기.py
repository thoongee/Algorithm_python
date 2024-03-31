import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().strip().split(' '))
mirro = []
for i in range(n):
    mirro.append(list(map(int, input().strip())))

dx = [-1,1,0,0] # 상하좌우
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque() 
    queue.append((x,y))# queue에 (x,y) 위치 튜플 쌍을 저장.
    # 현재 노드(start) 방문 처리
    mirro[x][y] = 2
    cnt = 0
    # queue가 빌때까지 반복
    while queue:
        # 하나의 원소를 뽑음    
        x,y = queue.popleft()
        cnt +=1 
        # 해당 원소와 '연결된', 괴물이 존재하지 않은 원소들을 queue에 삽입
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == (n-1) and ny==(m-1):
                mirro[nx][ny] = 2
                for j in range(len(mirro)):
                    print(mirro[j])
                cnt +=1
                return cnt
            if nx < 0 or ny <0 or nx>=n or ny>=m :
                continue
            if mirro[nx][ny]==1:
                queue.append((nx,ny))
                mirro[nx][ny] = 2 # 방문처리
    print(mirro)
    return cnt


res = bfs(0,0)
print(res)
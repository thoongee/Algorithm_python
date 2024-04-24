import sys
sys.setrecursionlimit(10000) # 재귀 호출 한도 증가
input = sys.stdin.readline

def dfs(x,y):
  if x<0 or y<0 or x>=n or y>=m:
    return False
  if graph[x][y] == 1:
    graph[x][y] = 0
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True
  return False

t = int(input().strip())
for _ in range(t):
  m,n,k = map(int,input().strip().split())

  # 배추 위치 입력받기
  graph = [[0]*m for _ in range(n)]
  for _ in range(k):
    x,y = map(int,input().strip().split())
    graph[y][x] = 1

  # 탐색 시작
  cnt = 0
  for i in range(n):
    for j in range(m):
      if dfs(i,j)==True:
        cnt +=1
  print(cnt)  


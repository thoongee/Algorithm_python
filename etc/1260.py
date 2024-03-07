# DFS, BFS : 트리 or 그래프 구조를 가지고 있어야 연결된 노드들을 파악 가능하다
# DFS : 인접행렬 방식으로 행과 열을 통해 값을 해당 숫자들이 연결되어 있는지 확인
# BFS : 큐

#N개의 숫자가 있으므로 N+1 x N+1의 행렬을 리스트를 통해서 만들고 0으로 채워준다. 인덱스와 값을 일치시키기 위해서 N+1개의 숫자를 사용한다.

#연결된 숫자들 값을 입력받아서 해당 행과 열의 값을 1로 바꿔준다. 이를 통해서 행의 숫자와 열의 숫자가 연결되어 있다는 표시를 해준다.

#처음엔 다른사람의 코드를 보고 공부를 하였고 이해한 뒤엔 다시 안보고 풀고를 반복하였으며 나중엔 문제만 보고 바로 풀 수 있게 되었다.
import sys
input = sys.stdin.readline

n,m,v = map(int,input().rstrip().split())

#인접 영행렬
matrix = [[0]*(n+1) for i in range(n+1)]

#방문한 곳 체크
visited = [0]*(n+1)

# 입력받는 두 값에 대해 영행렬에 1삽입
for i in range(m):
  a,b = map(int,input().rstrip().split())
  matrix[a][b] = matrix[b][a] = 1

def dfs(v):
  # 방문한 곳에 1 넣기
  visited[v] = 1
  print(v,end=' ')

  #재귀함수 선언
  #v와 인접한 곳을 찾고 방문하지 않았다면 함수 실행
  for i in range(1,n+1):
    if(visited[i]==0 and matrix[v][i]==1):
      dfs(i)

def bfs(v):
  #방문해야 할 곳을 순서대로 넣을 큐
  queue = [v]

  #dfs를 완료한 visited 배열(1로 되어있음)에서 0으로 방문체크
  visited[v] = 0

  #큐안에 데이터가 없을 때까지
  while queue:
    v = queue.pop(0)
    print(v,end=' ')
    for i in range(1,n+1):
      if (visited[i]==1 and matrix[v][i]==1):
        queue.append(i)
        visited[i] = 0

dfs(v)
print()
bfs(v)

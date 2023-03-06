import sys

input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())

visit = [[0]*m for _ in range(n)]  # 방문한 위치 저장
game_map = [] # 전체 맵 정보
for _ in range(n):
  row = list(map(int, input().split()))
  game_map.append(row)


dx = [-1, 0, 1, 0] # 북 동 남 서
dy = [0, 1, 0, -1]
visit[x][y] = 1  ## 현재 위치 = 가본 곳


# def turn_left(d):
#   if d == 0:
#     d = 3
#   else:
#     d -= 1
#   return d
def turn_left():
  global d
  d -= 1
  if d == -1:
    d = 3

cnt = 1
turn_time = 0
while True:
  turn_left()
  nx = x+dx[d]
  ny = y+dy[d]
  if visit[nx][ny]==0 and game_map[nx][ny]==0: # 정면에 가보지 않은 칸이 있을때, 이동
    d[nx][ny] = 1
    x = nx
    y = ny
    cnt += 1
    turn_time = 0
    continue
  else: # 정면에 가보지 않은 칸이 없거나, 바다인 경우
    turn_time += 1
  if turn_time == 4: #네 방향 모두 갈 수 없는 경우
    nx = x - dx[d]
    ny = y - dy[d]
    if game_map[nx][ny]==0: # 뒤로 갈 수 있다면 이동
      x = nx
      y = ny
    else: # 뒤가 바다일 경우
      break
    turn_time = 0
    
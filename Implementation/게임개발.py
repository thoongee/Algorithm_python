import sys

input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())
game_map = []
visit = []
for _ in range(n):
  row = list(map(int, input().split()))
  tmp = [0] * m
  game_map.append(row)
  visit.append(tmp)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visit[x][y] = 1  ## 현재 위치 = 가본 곳


def turn_left(d):
  if d == 0:
    d = 3
  else:
    d -= 1
  return d


check = True

while (check):
  d = turn_left(d)
  new_x = x + dx[d]
  new_y = y + dy[d]

  if game_map[new_x][new_y] == 0:
    x = new_x
    y = new_y

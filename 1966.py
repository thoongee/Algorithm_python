# point : 리스트 삽입, 삭제

import sys
input = sys.stdin.readline

case = int(input().rstrip())

for i in range(case):
  n,m = map(int, input().rstrip().split())
  level = list(map(int, input().rstrip().split()))
  
  position = [0 for _ in range(n)]
  position[m] = 1
  cnt = 0

  while True:
    if level[0] == max(level):
      cnt += 1

      if position[0] == 1:
        print(cnt)
        break
      else:
        del level[0]
        del position[0]

    else:
      level.append(level[0])
      position.append(position[0])
      del level[0]
      del position[0]


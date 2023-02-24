#브루트포스

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
chess=[]
res = []
b_list = ['B','W','B','W','B','W','B','W']
w_list = ['W','B','W','B','W','B','W','B']
b_start = [] #chess 1
w_start = [] #chess 2

#2가지 경우의 기본 8*8 chess
for i in range(4):
  b_start.append(b_list)
  b_start.append(w_list)
  w_start.append(w_list)
  w_start.append(b_list)

#chess 입력받기
for i in range(n):
  chess_col = list(input().strip())
  if len(chess_col) == m: #이건 필요한 조건인가?
    chess.append(chess_col)


for i in range(n-7): #8*8이니까
  for j in range(m-7):
    wcnt = 0
    bcnt = 0
    for x in range(8):
      for y in range(8):
        if chess[i+x][j+y] == w_start[x][y]:
          pass
        else:
          wcnt += 1
        if chess[i+x][j+y] == b_start[x][y]:
          pass
        else:
          bcnt += 1
    res.append(min(bcnt,wcnt))
    
print(min(res))


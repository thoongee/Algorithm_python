import sys
input = sys.stdin.readline

# map 생성
n = int(input())
# tmp_list = [1]*n
# map_list = []
# for _ in range(n):
#     map_list.append(tmp_list)

x,y = 0,0
dx = [0,1,0,-1] # R, D, L, U
dy = [1,0,-1,0]

move_list = input().strip().split(' ')
for move in move_list:
    if move == 'R':
        if dy[0]+y <n: # 공간을 벗어나지 않는지 확인
            y += dy[0] # 좌표 업데이트
    elif move == 'D':
        if dx[1]+x <n: 
            x += dx[1] 
    elif move == 'L':
        if 0<= dy[2]+y:
            y += dy[2]
    elif move == 'U':
        if 0<= dx[3]+x:
            x += dx[3]

print(x+1, y+1)

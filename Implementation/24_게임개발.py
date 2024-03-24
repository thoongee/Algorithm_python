import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split(' '))
a, b, d = map(int, input().strip().split(' '))

# 전체 맵 정보를 입력받기
map_list = []
for i in range(n):
    map_list.append(list(map(int, input().split())))

map_list[a][b] = 2 # 현재 위치 방문 처리

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def change_d(d):
    return (d - 1) % 4

move_cnt = 1
turn_time = 0

while True:
    d = change_d(d)
    nx = a + dx[d]
    ny = b + dy[d]

    if 0 <= nx < n and 0 <= ny < m and map_list[nx][ny] == 0:
        map_list[nx][ny] = 2
        a = nx
        b = ny
        move_cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    if turn_time == 4:
        nx = a - dx[d]
        ny = b - dy[d]
        if map_list[nx][ny] == 0:
            a = nx
            b = ny
        else:
            break
        turn_time = 0

print(move_cnt)
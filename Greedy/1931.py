import sys
input = sys.stdin.readline

n = int(input().strip())
rooms = []

for _ in range(n):
    start,end = map(int,input().strip().split())
    rooms.append((start,end))

sort_rooms= sorted(rooms, key=lambda x: (x[1], x[0]))

start, end = sort_rooms[0]
cnt = 1
for i in range(1,n):
    if end <= sort_rooms[i][0]:
        cnt +=1
        start = sort_rooms[i][0]
        end = sort_rooms[i][1]

print(cnt)
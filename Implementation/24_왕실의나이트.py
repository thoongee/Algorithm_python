import sys
input = sys.stdin.readline

point = input().strip()
row = point[-1]
col = 0
col_str = ['a','b','c','d','e','f','g','h']
# a 면 1로 변경
for i in range(len(col_str)):
    if point[0]==col_str[i]:
        col = i+1

move = [[1,2],[-1,2],[-2,1],[-2,-1],[2,1],[2,-1],[-2,1],[-2,-1]]

cnt = 0
for i in range(len(move)):
    nx = int(row)+move[i][0]
    ny = col+move[i][1]
    if nx <1 or nx>8 or ny <1 or ny>8:
        continue
    cnt +=1
print(cnt)
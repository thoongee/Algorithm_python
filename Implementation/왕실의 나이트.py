import sys

input = sys.stdin.readline

now = input()
pos = [1,1]

pos[1] = int(now[1])
if now[0]=='a':
  pos[0] = 1
elif now[0]=='b':
  pos[0] = 2
elif now[0]=='c':
  pos[0] = 3
elif now[0]=='d':
  pos[0] = 4
elif now[0]=='e':
  pos[0] = 5
elif now[0]=='f':
  pos[0] = 6
elif now[0]=='g':
  pos[0] = 7
else:
  pos[0] = 8

# print(pos)
new_pos = [0,0]
cnt = 0
move= [[-1,-2],[1,-2],[-1,2],[1,2],[-2,-1],[-2,1],[2,-1],[2,1]]
for i in range(len(move)):
  new_pos[0] = pos[0]+move[i][0]
  new_pos[1] = pos[1]+move[i][1]
  if 0<new_pos[0]<9 and 0<new_pos[1]<9:
    cnt +=1

print(cnt)

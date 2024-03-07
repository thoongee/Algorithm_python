import sys
input = sys.stdin.readline

n = int(input().rstrip())
n_list = []
mark = []
add = 0

for i in range(1,n+1):
  x = int(input().rstrip())

  if not n_list:
    for j in range(i,x+1):
      add = j+1
      n_list.append(j)
      mark.append('+')

  elif n_list[-1] < x:
    for j in range(add,x+1): # 한번 더했던건 넘어가야 하는데, 또 더함
      add = j+1
      n_list.append(j)
      mark.append('+')

  if n_list[-1] == x:
    n_list.pop()
    mark.append('-')


if not n_list:
  for i in mark:
    print(i)
else:
  print('NO')

import sys
input = sys.stdin.readline
#입력을 어떻게 받아서 저장할지 생각하게 되는 문제
while True:
  num_list= list(map(int,input().rstrip()))
  if num_list[0]==0:
    break

  check = -1
  high = len(num_list)-1
  for i in range(high):
    if i >= (high-i):
      break
    if num_list[i] != num_list[high-i]: #index out of range
      check += 1
    
  if check != -1:
    print('no')
  else:
    print('yes')


    
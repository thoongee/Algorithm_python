#스택구현
#list.pop은 존재
#list.push 대신 .append 이용
import sys
input = sys.stdin.readline

n = int(input().rstrip())
n_list = [] # 스택
mark = [] # + - 
add = 0 # 더했던 수를 또 더하지 않도록

for i in range(1,n+1):
  x = int(input().rstrip())

  if not n_list: #비었을 때
    for j in range(i,x+1): # 입력받은 수까지 push
      add = j+1
      n_list.append(j)
      mark.append('+')
      # print('if')
      # print(n_list)
      # print(mark)
  elif n_list[-1] < x: # 입력받은 수가 리스트의 끝 값보다 클 때
    for j in range(add,x+1): # 입력받은 수까지 push
      add = j+1
      n_list.append(j)
      mark.append('+')
      # print('elif 1')
      # print(n_list)
      # print(mark)
  if n_list[-1] == x: # 입력받은 수가 리스트의 끝 값과 같을때 pop
    n_list.pop()
    mark.append('-')
    # print('if 2')
    # print(n_list)
    # print(mark)

if not n_list: #리스트가 비었을 때
  for i in mark:
    print(i)
else: #리스트가 비어있지 않을 때
  print('NO')

# if, elif 조건 헷갈
# 문제1. 4를 입력하면 4까지 append해야하는데, 하나만 append를 함 --> for문 추가
# 문제2. 한번 더했던 값은 넘어가야 하는데, 삭제된 값부터 또 더함 --> add 변수 추가
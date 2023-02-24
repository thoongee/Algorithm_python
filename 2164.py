# point : 리스트 삭제, 삽입

# 시간초과 --> 어디서?

# queue
import sys
input = sys.stdin.readline

N = int(input().rstrip())
L = list(range(1,N+1)) 

while (len(L)>1): 
  L.pop(0) 
  temp = L.pop(0)
  L.append(temp) 
  
print(L.pop(0))

# 아이디어 : deque
# 양 방향으로 추가, 삭제 가능

import sys
input = sys.stdin.readline

from collections import deque

n = int(input()) 
deque = deque([i for i in range(1, n+1)]) 

while(len(deque) >1): 
  deque.popleft() 
  move_num = deque.popleft()
  deque.append(move_num) 
  
print(deque[0])

import sys
from collections import deque
input = sys.stdin.readline
n,k = map(int, input().strip().split())

queue = deque([i for i in range(1,n+1)])
print("<",end='')

while queue:
    for _ in range(k-1): # queue의 맨 앞에 있는 원소를 꺼내서 뒤에 append. 이걸 k-1번 반복. 
        queue.append(queue.popleft())
    print(queue.popleft(),end='') # k번째 원소 pop
    if queue: # queue가 비어있지 않다면
        print(', ',end='') # 출력 형태 맞춰 출력하기

print('>')

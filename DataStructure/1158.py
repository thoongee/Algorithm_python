import sys
from collections import deque
input = sys.stdin.readline
n,k = map(int, input().strip().split())

queue = deque([i for i in range(1,n+1)])
print("<",end='')

while queue:
    for _ in range(k-1):
        queue.append(queue.popleft())
    print(queue.popleft(),end='')
    if queue:
        print(', ',end='')

print('>')

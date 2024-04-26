import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

visited=[False]*100001

def bfs(x):
    sec = 0
    queue = deque([(x,sec)])
    visited[x]=True
    while queue:
        x,time = queue.popleft()
        if x == k:
            return time
        if x-1>=0 and not visited[x-1]:
            visited[x-1] = True
            queue.append((x-1,time+1))
        if x+1<=100000 and not visited[x+1]:
            visited[x+1] = True
            queue.append((x+1,time+1))
        if 2*x <=100000 and not visited[2*x]:
            visited[2*x] = True
            queue.append((2*x,time+1))


res = bfs(n)
print(res)
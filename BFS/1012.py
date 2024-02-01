from collections import deque

t = int(input())
for _ in t:
  m,n,k = map(int, input().split())
  graph = []
  for i in k :
    x,y = map(int, input().split())
    graph.append(list(x,y))

import sys
input = sys.stdin.readline

n,m = map(int, input().strip().split())

graph=[]

for _ in range(m):
  graph.append(list(int,input().strip().split()))
  
  

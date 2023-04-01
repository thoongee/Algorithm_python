import sys

input = sys.stdin.readline

def find(x):
  if x == parent[x]:
    return x
  parent[x] = find(parent[x])
  return parent[x]

def union(x, y):
  x = find(x)
  y = find(y)
  if x != y:
    parent[y] = x
    cnt[x] += cnt[y]


n = int(input())
for _ in range(n):
  f = int(input())
  parent = {}
  cnt = {}
  for _ in range(f):
    a, b = input().split()
    if a not in parent:
      parent[a] = a
      cnt[a] = 1
    if b not in parent:
      parent[b] = b
      cnt[b] = 1
    union(a, b)
    print(cnt[find(a)])
import sys
input = sys.stdin.readline

T = int(input().rstrip())

d = [0]*12
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(T):
  n = int(input().rstrip())
  
  for j in range(4,n+1):
    d[j] = d[j-1]+d[j-2]+d[j-3]

  print(d[n])

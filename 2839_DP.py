import sys
input = sys.stdin.readline

n = int(input())
re = [5001]*(n+5)
re[3] = 1
re[5] = 1

for i in range(6,n+1):
  re[i] = min(re[i-3]+1, re[i-5]+1)

if re[n] >= 5000:
  print(-1)
else:
  print(re[n])
  
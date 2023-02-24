import sys
input = sys.stdin.readline

n = int(input().rstrip())

cnt = [0]*1001
cnt[1] = 1
cnt[2] = 2

for i in range(3,n+1):
  cnt[i] = cnt[i-1]+cnt[i-2]

print(cnt[n]%10007)

##################################

import sys
input = sys.stdin.readline

n = int(input().rstrip())

cnt = [0,1,2]

for i in range(3,n+1):
  cnt[i].append(cnt[i-1]+cnt[i-2])

print(cnt[n]%10007)
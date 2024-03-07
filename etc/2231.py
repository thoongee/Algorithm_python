# ValueError --> 왜?

import sys
input = sys.stdin.readline

n = int(input())
m = []

for i in range(1, n+1):
    div_num = list(map(int, str(i)))
    sum_num = i + sum(div_num) #분해합

    if(sum_num == n):
        m.append(i)
        break

if len(m)==0:
  print(0)
else:
  print(min(m))
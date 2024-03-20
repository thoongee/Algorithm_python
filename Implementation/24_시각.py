import sys
input = sys.stdin.readline

n = int(input())
k = 0
for i in range(1,54): # 59까지지만, 53이 가장 마지막에 count되는 수라는 걸 알기 때문에.
    if '3' in str(i):
        k +=1

k = k*k
j = 0

for i in range(n+1):
    if '3' in str(i):
        j +=1

total = k * j

print(total)


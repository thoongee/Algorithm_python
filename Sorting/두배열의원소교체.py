import sys
input = sys.stdin.readline


n,k = map(int,input().strip().split(' '))
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))

# a,b를 먼저 sorting 해두고 시작해도 되나..?
a.sort()
b.sort()

i = 0
j = n-1

for cnt in range(k):
    if a[i]<b[j]:
        a[i], b[j] = b[j] , a[i]
        i += 1
        j -= 1
    else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출 (이거 생각못함)
        break

print(sum(a))

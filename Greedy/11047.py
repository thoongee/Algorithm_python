import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())

coins = [int(input()) for _ in range(n)]

coins.sort(reverse=True)

cnt = 0

for coin in coins:
    # 구하고자 하는 k가 coin으로 나누어진다면
    if k // coin > 0:
        cnt += k // coin
    # 나누고 난 나머지를 k에 재할당
    k %= coin
    
print(cnt)

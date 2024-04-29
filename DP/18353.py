import sys
input = sys.stdin.readline

n = int(input().strip())
array = list(map(int, input().split()))

# 주어진 문제 : 가장 긴 감소하는 부분 수열’의 길이를 계산하는 문제
# 순서를 뒤집어 '가장 긴 증가하는 부분 수열' 문제로 변환
array.reverse()

# 1차원 DP 테이블 초기화
dp = [1] * n

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 열외시켜야 하는 병사의 최소 수 = 초기 병사 수 - LIS 길이
print(n - max(dp))
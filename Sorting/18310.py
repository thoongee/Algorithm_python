import sys
input = sys.stdin.readline

n = int(input().strip())
data = list(map(int, input().strip().split()))
data.sort()
# 중간값(median)을 출력
print(data[(n - 1) // 2])

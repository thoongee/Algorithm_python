def modular_pow(a, b, c):
    if b == 0:
        return 1
    elif b == 1:
        return a % c
    else:
        half = modular_pow(a, b // 2, c)
        half = half * half % c
        if b % 2 == 1:
            half = half * a % c
        return half

import sys
input = sys.stdin.read

# 입력을 받습니다.
a, b, c = map(int, input().strip().split())

# 결과를 계산하고 출력합니다.
result = modular_pow(a, b, c)
print(result)
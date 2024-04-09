# 괄호 갯수가 맞으면 VPS가 아니라, 괄호가 잘 닫혀있으면 VPS이다.

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    ps = input().strip()
    while '()' in ps:
        ps.replace('()','')
    
    if ps: # ps가 비어있다면
        print('NO')
    else:
        print('YES')
        
import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):

    s = input().strip() # 문자열 입력 받음

    while '()' in s: # 문자열 탐색
        s = s.replace('()','') # string 내에 어디든, ()이 있다면 삭제

    print('NO') if s else print('YES')

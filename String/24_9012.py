import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):

    s = input().strip() # 문자열 입력 받음

    while '()' in s: # 문자열 탐색
        s = s.replace('()','') # string 내에 어디든, ()이 있다면 삭제

    print('NO') if s else print('YES')
'''
import sys
input = sys.stdin.readline

t = int(input().strip())

# stack 구조 활용
for _ in range(t):
    ps = input().strip()# 입력받은 괄호 문자열

    stack = []

    for x in ps:
        # ( 을 입력받으면, stack에 push
        if x == '(':
            stack.append(x)
        
        # ) 을 입력받았을 때
        elif x == ')' :
            if len(stack)==0:
                # stack이 비어있다면
                stack.append(x)
            elif stack[-1]=='(':
                # 제일 상단에 ( 이 있다면 pop
                stack.pop()
            elif stack[-1]==')':
                # 제일 상단에 ) 이 있다면 append
                stack.append(x)
            

    if stack: # stack이 비어있지 않다면
        print('NO')
    else:
        print('YES')
'''
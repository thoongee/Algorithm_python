# 괄호 갯수가 맞으면 VPS가 아니라, 괄호가 잘 닫혀있으면 VPS이다.

import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    stack = []
    ps_group = input().strip()
    for ps in ps_group:
        if stack: # stack에 무언가 있다면
            if ps =='(':
                stack.append(ps)
            elif ps==')':
                if stack[-1]=='(': # stack 제일 끝에 ( 가 있다면
                    stack.pop()
                else: # stack 제일 끝에 )가 있다면
                    stack.append(ps)

        else: # stack이 비어있다면
            stack.append(ps)

    if stack: # stack에 괄호가 남아있다면
        print("NO")
    else:
        print("YES")

# sum 

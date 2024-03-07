import sys
input = sys.stdin.readline

# 이와 같이 함수를 사용하는 경우, 재사용성, 가독성, 유지보수성 측면에서 장점이 있음

def push(stack,x):
    stack.append(x)
    # return stack 할 필요 없음 : 리스트는 가변 객체이므로, 함수 내에서 변경하면 원본 리스트도 변경됌

def pop(stack):
    if not stack: ## list가 비었는지 확인
        print(-1)
    else:
        print(stack.pop())

def empty(stack):
    if not stack:
        print(1)
    else:
        print(0)

def size(stack):
    print(len(stack))

def top(stack):
    if not stack:
        print(-1)
    else:
        print(stack[-1])


n = int(input().strip()) # strip() : 마지막 개행문자 제거
stack = []

for _ in range(n):
    command = list(input().strip().split()) # ['push','1']
    if command[0]=='push':
        push(stack,int(command[1]))
    elif command[0]=='pop':
        pop(stack)
    elif command[0]=='size':
        size(stack)
    elif command[0]=='empty':
        empty(stack)
    elif command[0]=='top':
        top(stack)

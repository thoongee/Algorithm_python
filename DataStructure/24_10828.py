import sys
input = sys.stdin.readline


def push(stack,x):
    stack.append(x)

def pop(stack):
    if not stack: 
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


n = int(input().strip()) 
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

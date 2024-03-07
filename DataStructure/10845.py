import sys
input = sys.stdin.readline

dat =[]
head = 0
tail = 0
N = int(input())
for i in range(N):
    command = list(input().split())

    if command[0]=='push':
        dat.append(command[1])
        tail += 1

    elif command[0]=='pop':
        if head==tail:
            print(-1)
        else:
            print(dat[head])
            dat[head] = None
            head += 1

    elif command[0]=='size':
        print(tail-head)

    elif command[0]=='empty':
        if head == tail:
            print(1)
        else:
            print(0)
    elif command[0]=='front':
        if head == tail:
            print(-1)
        else:
            print(dat[head])
    elif command[0]=='back':
        if head == tail:
            print(-1)
        else:
            print(dat[tail-1])

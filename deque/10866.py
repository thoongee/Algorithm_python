import sys
input = sys.stdin.readline

N = int(input())
mid = 5000
deque = [None for i in range(10000)] # N의 범위가 1~10000
head = mid # 시작지점 = 배열의 중간
tail = mid # 마지막 원소의 index+1
# print(deque)
# print(len(deque))

for _ in range(N):

    command = list(input().split())

    if command[0]== 'push_front':
        head -= 1
        # deque.insert(head,int(command[1])) # 처음에 deque를 None으로 채워두고 시작하니까, insert를 하면 그 값이 추가되어버림 (대체가 아니라)
        deque[head] = int(command[1])
        # print(deque)
        # print('head',head)

    if command[0]== 'push_back':
        # deque.insert(tail, int(command[1]))
        deque[tail] = int(command[1])
        tail += 1
        # print(deque)
        # print('tail',tail)

    if command[0]=='pop_front':
        if head == tail:
            print(-1)
        else:
            print(deque[head])
            # del deque[head] # pos만 옮겨주면 되는줄 -> 그래도 될걸? 나중에 덮어쓸거니까
            head += 1
            # print(deque)
            # print('head',head)

    if command[0]=='pop_back':
        if head == tail:
            print(-1)
        else:
            tail -= 1
            print(deque[tail])
            # print(deque)
            # print('tail',tail)
            # del deque[tail] # pos만 옮겨주면 되는줄

    if command[0]=='size':
        print(tail-head)
        # print(deque)

    if command[0]=='empty':
        if head == tail:
            print(1)
        else:
            print(0)

    if command[0] == 'front':
        if head == tail:
            print(-1)
        else:
            print(deque[head])
            # print(deque)

    if command[0] == 'back':
        if head == tail:
            print(-1)
        else:
            print(deque[tail-1])
            # print(deque)



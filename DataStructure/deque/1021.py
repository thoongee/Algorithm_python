# 문제를 이해하는데 시간이 좀 걸렸다
# 예제 입력 2를 시행하면 내 생각엔 5가 출력인데, 왜 8인지.. --> 이 문제에서는 뒤에서는 뺄 수 없다! 앞에서만 원소를 뺄 수 있다
# queue : FIFO
# deque : 양방향에서 삽입, 삭제 가능 (but 이문제에서는 뒤에서 빼는 기능은 사용하지 않음!)

from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
pos = list(map(int, input().split()))
dq = deque([i for i in range(1,n+1)])
count = 0
for i in pos:
    #1번
    while True: # 이거이거 꼭 넣기!
        if dq[0]== i: # 덱의 첫번째 원소 == 뽑으려고 하는 수 일때,
            dq.popleft()
            break # while문 탈출! 다음 입력값으로 이동
        else:
            #2번 : 뽑으려는 수가 deque의 앞부분에 있을때,
            if dq.index(i) < len(dq)/2: # len(dq)대신 n 넣으면 안됌! pop 된게 있으면 길이가 달라지거든
                while dq[0] !=i: # deque의 첫번째 원소 == 뽑으려고 하는 수 가 될때까지 왼쪽으로 한칸이동
                    dq.append(dq.popleft())
                    count+=1
            #3번 : 뽑으려는 수가 deque의 뒷부분에 있을 때,
            else:
                while dq[0] !=i:
                    dq.appendleft(dq.pop()) # deque의 첫번째 원소 == 뽑으려고 하는 수 가 될때까지 오른쪽으로 한칸 이동
                    count+=1

sys.stdout.write(str(count)) # print보다 조금 더 빠르게 출력할 수 있으나, str형식이어야 함
# print(count)

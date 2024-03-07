# 백준에서 확인했을 땐, 이 코드가 60ms에 약 20000KB 메모리 였는데, 내가 직접 올려보니 내가 처음에 작성한 코드와 메모리

import sys
t = int(input())
q = []
res = []
L = sys.stdin.read().splitlines() 
# 입력값을 한줄마다 나누어서 L list에 저장
# 입력값의 끝을 알려주는 신호 EOF(End Of File) : 윈도우에서는 Ctrl + z 리눅스, 맥에서는 Ctrl + d

for idx in range(t):
    a,*b = L[idx].split()
    if "push" in a:
        q.append(b[0])
    elif a == "front":
        res.append(q[0] if q else "-1") # if q == q에 원소가 있으면
    elif a == "back":
        res.append(q[-1] if q else "-1")
    elif a == "size":
        res.append(str(len(q)))
    elif a == "empty":
        res.append('0' if q else "1")
    elif a == "pop":
        res.append(q.pop(0) if q else "-1")
print("\n".join(res))

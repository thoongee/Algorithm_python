# Dynamic programming
# 시간초과 --> 어디에서 시간줄이지?
# 규칙을 찾아야함!
import sys
input = sys.stdin.readline

cnt_0 = 0
cnt_1 = 0
 
def fibo(n):
    # 전역변수
    global cnt_0
    global cnt_1 
 
    if n==0:
        cnt_0 +=1
        return 0
    elif n==1:
        cnt_1 +=1
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
 
t = int(input().rstrip())
 
for _ in range(t):
  fibo(int(input().rstrip()))
  print(cnt_0, cnt_1)
  cnt_0 = 0
  cnt_1 = 0

# 손으로 그려서 규칙을 찾음 (n,cnt_0,cnt_1의 갯수)
# 0의 갯수 = 이전 1의 개수
# 1의 개수 = 이전 0+1의 개수
t = int(input())
 
for _ in range(t):
  cnt_0 = [1,0]
  cnt_1 = [0,1]
  n = int(input())
  if n>1:
    for i in range(n-1):
      cnt_0.append(cnt_1[-1])
      cnt_1.append(cnt_0[-2]+cnt_1[-1]) 
 
  print(cnt_0[n], cnt_1[n])


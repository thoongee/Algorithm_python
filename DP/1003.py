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
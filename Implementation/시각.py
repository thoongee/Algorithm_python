# 완전탐색 (Brute Forcing) : 모든 가능한 경우를 검사해보는 탐색법
# 아이디어 : 시간 -> 문자열로 변형, 문자열에 특정 값이 들어있는지 확인

import sys
input = sys.stdin.readline

n = int(input())

cnt = 0
for i in range(n+1):
  for j in range(60):
    for k in range(60):
      # print('시간 : ',str(i) + str(j) + str(k))
      if '3' in str(i) + str(j) + str(k):
        cnt += 1

print(cnt)

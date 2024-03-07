#에라토스테네스의 체 : 소수 판별 알고리즘, 2부터 시작해서 특정 숫자의 배수에 해당하는 숫자들을 모두 지움
#소수 : 1과 자기자신만을 약수로 가지는 수

#왜 i=9, j=2일때 한번밖에 실행이 안되지?? --> 나눠지지 않을때 1로 바꾸니까 9의 경우에 2에서 1로 바뀌고, 이후에도 1이 계속 남아있어서 결과적으로 소수로 취급된 것임 --> 소수가 아닐때 1로 바꾸는것으로 변경

#문제1. 시간초과 --> 대체 왜..??
import sys
import math
input = sys.stdin.readline

m,n = map(int,input().rstrip().split())

prime = [0 for i in range(n+1)] #초기화

for i in range(m,n+1):
  # sqrt = int(i**0.5)
  sqrt = int(math.sqrt(i))
  # print('i, sqrt: ',i,sqrt)

  for j in range(2,sqrt+1):
    if i%j == 0: # 나눠지는 수가 있을 때
      prime[i] = 1
      # print('i,j: ',i,j)
  if prime[i] == 0: #출력->시간초과x
    print(i)
    

# 1이 저장된 인덱스만 출력
# for i in range(2,n+1):
#   if prime[i] == 0:
#     print(i)


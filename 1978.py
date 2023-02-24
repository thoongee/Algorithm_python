# import sys
# input = sys.stdin.readline

# N = int(input())

# num_list = []

# num_list=map(int, input().rstrip().split())

# cnt=0

# for i in num_list:
#     #에라토스테네스의 체
#     check = 0
#     if i > 1:
#         for j in range(2, i//2+1):    
#             if (i%j == 0):
#                 check += 1 #배수는 배열에서 제거 
#         if check == 0:
#             cnt+=1 #배수가 아님 
# print(cnt)


### 에라토스테네스의 체
import sys 
input = sys.stdin.readline

N = int(input()) 
target = list(map(int, input().rstrip().split())) 

prime = [1] * 1001 
prime[0], prime[1] = 0, 0 # check prime number 

for i in range(2, 1001): 
  if prime[i]: # prime[i] 기본 : 1
    jmp = 2 
    while i * jmp <= 1000: # jump. 2*2, 2*3, 2*4 .. : 2의 배수
      prime[i*jmp] = 0  # 배수는 다 prime을 0으로 변경
      jmp += 1
      
res = 0 
for t in target: 
  if prime[t]: 
    res += 1 # prime이 1인것만 res 추가
          
# sys.stdout.write(str(res))
print(res)


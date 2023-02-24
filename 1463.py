# 동적프로그래밍
# 작은 수부터 (2부터) 1로 만드는 횟수 저장
# cnt의 index : 입력한 숫자 n
# index에 위치한 값 : 연산의 최솟값
import sys
input = sys.stdin.readline

n = int(input().rstrip())
cnt = [0]*(n+1)

for i in range(2,n+1):
  
  cnt[i] = cnt[i-1]+1
  
  if i%3==0:
    cnt[i] = min(cnt[i],cnt[i//3]+1)
  
  if i%2 ==0:
    cnt[i] = min(cnt[i],cnt[i//2]+1)

print(cnt[n])
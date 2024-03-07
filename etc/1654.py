#이분탐색
#정렬된 배열에서 탐색범위를 반씩 줄여가며 값을 탐색하는 방법

#왜 200이 아니고 199가 나오지?
#low는 0이아니고 1로 설정!

#시간초과
#시도1. 리스트를 입력받으면서 정렬? x
#시도2. 리스트 정렬 말고 high = min(lan)설정 x
#시도3. high = max(lan)
import sys
input = sys.stdin.readline

k,n = map(int,input().rstrip().split())


lan = []
for _ in range(k):
  lan.append(int(input().rstrip()))

cnt = 0
low = 1
high = min(lan)

while True:
  mid = (low+high)//2

  for i in range(k):
    cnt += lan[i]//mid

  if cnt == n:
    print(mid)
    break
  elif cnt < n:
    cnt = 0
    high = mid
  elif cnt > n:
    cnt = 0
    low = mid



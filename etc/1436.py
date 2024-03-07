#cnt를 결과로 내는게 아니라, cnt를 입력받고 해당하는 숫자를 결과로 내야하네
#어렵다

import sys
input = sys.stdin.readline

n = int(input().rstrip())
cnt = 0
num = 666

while True:
  if "666" in str(num): #문자열에 특정 문자열이 포함되었는지 확인
    cnt += 1
  if cnt == n:
    break
  num += 1 #666부터 1씩 증가하면서 쭉 탐색

print(num)
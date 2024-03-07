# point1. 띄어쓰기 구분하여 여러개의 값을 입력받아, 리스트로 저장하기

#point2. 리스트에 특정 값이 있는지 확인하기

import sys
input = sys.stdin.readline

n = int(input().rstrip())

a = set(input().rstrip().split())

m = int(input().rstrip())
check_num = input().rstrip().split()
check = []

# 여기서 시간초과가 난것 같다
# set, dictionary의 in연산을 통한 포함 여부 확인 : O(1)
# 값이 존재하는지 여부만 알면 됌 --> a를 set 자료형으로 변경
# 굳이 int자료형일 필요x
for i in check_num: #O(n)
  if i in a:
    print(1)
  else:
    print(0)

#이게 왜 이분탐색, 트리를 사용한 집합과 맵이지?
#이분탐색 : O(logn)
import sys
input = sys.stdin.readline

n = int(input().rstrip())
n_set = set(input().rstrip().split())

m = int(input().rstrip())
m_li = input().rstrip().split()
check = []

# set, dictionary의 in연산을 통한 포함 여부 확인 : O(1)
# 값이 존재하는지 여부만 알면 됌 --> a를 set 자료형으로 변경
# 굳이 int자료형일 필요x

for i in m_li: #O(n)
  if i in n_set:
    print(1)
  else:
    print(0)
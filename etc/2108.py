from collections import Counter
import sys
input = sys.stdin.readline

n = int(input()) # n은 홀수
n_list = []

for i in range(n):
  n_list.append(int(input().rstrip()))

n_list.sort()


def mean(n,n_list):
  hap = 0
  for i in n_list:
    hap += i
  
  return(round(hap/n))


def mid(n,n_list):
  return(n_list[n//2])


## 아이디어1. input 값 = my_list의 index
def many(n_list): #최빈값 : 쉽지않네

  n_cnt = Counter(n_list) # 딕셔너리, (숫자 : 빈도)

  n_cnt = n_cnt.most_common() # 빈도수가 높은순으로 정렬, 튜플

  if len(n_list) >= 2: 
      if n_cnt[0][1] == n_cnt[1][1]: #최빈값이 1개 이상일 때
          return n_cnt[1][0]
      else:
          return n_cnt[0][0]
  else: # 입력값이 하나일때
      return n_list[0]


def scope(n_list):
  return n_list[n-1]-n_list[0]


print(mean(n,n_list))
print(mid(n,n_list))
print(many(n_list))
print(scope(n_list))
"""
"""
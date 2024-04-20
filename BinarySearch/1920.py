import sys
input = sys.stdin.readline

def binary_search(arr, x):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < x:
            start = mid + 1
        elif arr[mid] > x:
            end = mid - 1
        else: # arr[mid] == x
            return True
    return False

n = int(input().strip())
n_li = sorted(list(map(int, input().strip().split())))
m = int(input().strip())
m_li = list(map(int, input().strip().split()))

for m in m_li:
    if binary_search(n_li, m):
        print(1)
    else:
        print(0)

# import sys
# input = sys.stdin.readline

# n = int(input().rstrip())
# n_set = set(input().rstrip().split()) # 굳이 int자료형일 필요x
# print(n_set)
# m = int(input().rstrip())
# m_li = input().rstrip().split() # 굳이 int자료형일 필요x

# # set, dictionary의 in연산을 통한 포함 여부 확인 : O(1)
# # 값이 존재하는지 여부만 알면 됌 --> a를 set 자료형으로 변경

# for i in m_li: #O(n)
#   if i in n_set:
#     print(1)
#   else:
#     print(0)
import sys
input=sys.stdin.readline
from collections import Counter

#이분 탐색 알고리즘

n,m=map(int, input().split())
trees=Counter(map(int, input().split()))

s = 1
e = max(trees)

while s<=e:
    mid = (s+e)//2 #중간값
    tot=sum( (h-mid) * i for h,i in trees.items() if h>mid)

    if tot>=m: #가져갈 수 있는 나무 길이 합이  목표보다 크거나 같은 경우
        s = mid+1 #높이를 높여야
    elif tot<m: #가져갈 수 있는 나무길이 합이 목표보다 작은 경우
        e = mid-1 #높이를 낮춰야 함

print(e)
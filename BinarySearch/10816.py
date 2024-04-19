import sys
from collections import Counter
input = sys.stdin.readline

n = int(input().strip())
n_li = Counter(list(map(int,input().strip().split())))
m = int(input().strip())
m_li = list(map(int,input().strip().split()))


res_li = []

for value in m_li:
    res_li.append(n_li[value])

print(' '.join(map(str,res_li)))

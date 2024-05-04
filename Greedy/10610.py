import sys
input = sys.stdin.readline

n_li = list(input().strip())
sorted_n = sorted(n_li,reverse=True)
str_n = ''
for s in sorted_n:
    str_n += s

if '0' not in str_n or int(str_n)%30!=0:
    print(-1)
else:
    print(str_n)

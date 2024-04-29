import sys
input = sys.stdin.readline

n = int(input())
p_list = list(map(int,input().strip().split(' ')))

sorted_li = sorted(p_list)
time = 0
for i in range(1,len(sorted_li)+1):
	time += sum(sorted_li[:i])

print(time)

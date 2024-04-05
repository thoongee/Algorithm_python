import sys
input = sys.stdin.readline

n = int(input().strip())

# 너무 코드가 1차원적인데..
num_list = []
for _ in range(n):
    number = int(input().strip())
    num_list.append(number)

num_list.sort()
for i in num_list:
    print(i)
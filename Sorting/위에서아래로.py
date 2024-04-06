import sys
input = sys.stdin.readline

# 수의 개수가 500개 이하로 매우 적으며, 모든 수는 1 이상 100,000 이하이므로 어떠한 정렬 알고리즘을 사용해도 문제를 해결할 수 있다
n = int(input().strip())

num_list = []
for _ in range(n):
    num = int(input().strip())
    num_list.append(num)

num_list.sort(reverse=True)

for i in num_list:
    # print(i,'\t')
    print(i, end=' ')
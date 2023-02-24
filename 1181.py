import sys
input = sys.stdin.readline #문자열에 개행문자\n 자동추가

n = int(input())
n_list = []
for i in range(n):
  x = input().strip()
  if x not in n_list:
    n_list.append(x)

#n_list = set(n_list) #'set'object has no attribute 'sort'
n_list.sort(key = lambda x : len(x))
print(n_list)

for i in range(n-1): #0~11
  if len(n_list[i]) == len(n_list[i+1]): #0~12
    n_list[i:i+1] = sorted(n_list[i:i+1]) #부분정렬, 순차정렬
  #   n_list.sort()를 하면 다 알파벳 순으로 바뀌어버리잖아
  # 일부만 알파벳 순으로 할 수 있는 방법은?

print(n_list)

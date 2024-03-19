import sys
input = sys.stdin.readline

n = int(input())
p_list = list(map(int,input().strip().split(' ')))

# 시간 복잡도가 가장 짧은 정렬 방식 : merge sort, heap sort
# 메모리 측면에서는 merge sort보다 quick sort가 더 좋음
# 메모리+시간을 모두 고려하면 최악의 시간복잡도를 고려했을때, heap sort가 가장 좋음

# sorted 사용해도 메모리, 시간 측면에서 별 차이 안남. 
def merge_sort(array):
	if len(array) < 2:
		return array
	mid = len(array) // 2
	low_arr = merge_sort(array[:mid])
	high_arr = merge_sort(array[mid:])

	merged_arr = []
	l = h = 0
	while l < len(low_arr) and h < len(high_arr):
		if low_arr[l] < high_arr[h]:
			merged_arr.append(low_arr[l])
			l += 1
		else:
			merged_arr.append(high_arr[h])
			h += 1
	merged_arr += low_arr[l:]
	merged_arr += high_arr[h:]
	# print(merged_arr)
	return merged_arr

# sorted_li = merge_sort(p_list)
sorted_li = sorted(p_list)
time = 0
for i in range(1,len(sorted_li)+1):
	time += sum(sorted_li[:i])

print(time)

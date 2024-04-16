import sys
k,n = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(k)]
start = 1
end = max(lan)


while start <= end: # start > end 가 되기 전까지만 실행됌. 
    mid = (start + end) // 2 
    cnt = 0 # 랜선 수
    for i in lan:
        cnt += i // mid # mid 길이로 각 랜선을 잘랐을 때, 생기는 랜선들의 총 갯수
        
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
    

print(end)

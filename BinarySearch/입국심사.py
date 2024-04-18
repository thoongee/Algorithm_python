def solution(n, times):
    
    start = 0
    end = n*max(times)
    answer = end  # 최솟값을 저장할 변수
    while start <= end:
        mid = (start + end) // 2
        cnt = sum(mid // time for time in times)
        if cnt >= n:
            answer = min(answer, mid)  # 현재 mid 값이 최솟값인지 확인
            end = mid - 1
        else:
            start = mid + 1
    return answer
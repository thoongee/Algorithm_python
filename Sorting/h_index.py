def solution(citations):
    citations = sorted(citations) # 내림차순 정렬
    l = len(citations)
    for i in range(l): 
        if citations[i] >= l-i: 
        # l-i: 현재 검토 중인 논문을 포함하여 그 논문보다 더 많이 또는 같은 횟수로 인용된 논문의 수
        # citations[i] : i번째로 많이 인용된 논문의 인용 횟수
            return l-i # 조건을 만족하는 첫 번째 순간이 바로 최대 h-인덱스 값을 찾는 순간
    return 0
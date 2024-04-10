def solution(bridge_length, weight, truck_weights):
    time = 0  # 경과 시간
    bridge = []  # 다리를 건너는 트럭의 무게와 떠나는 시간을 저장
    bridge_weight = 0  # 다리 위의 트럭 무게 총합
    
    while truck_weights or bridge:
        time += 1  # 시간 증가
        
        # 다리를 건넌 트럭 제거
        if bridge and bridge[0][1] == time:
            bridge_weight -= bridge.pop(0)[0]
        
        # 새 트럭이 다리에 올라갈 수 있는지 확인
        if truck_weights and bridge_weight + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            bridge_weight += truck
            bridge.append([truck, time + bridge_length])  # 트럭 무게와 다리를 떠나는 시간 저장
        
    return time

# 테스트 케이스 실행
res = solution(2, 10, [7, 4, 5, 6])
print(res)
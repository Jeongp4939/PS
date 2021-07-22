from collections import deque

def solution(bridge_length, weight, truck_weight):
    cnt = 0
    on_bridge = deque([0]*bridge_length)        # 다리의 길이만큼 0 배열 deque 로 생성
    truck_weight = deque(truck_weight)

    while on_bridge:
        cnt += 1
        on_bridge.popleft()
        if truck_weight:
            if sum(on_bridge) + truck_weight[0] <= weight:
                on_bridge.append(truck_weight.popleft())
            else:
                on_bridge.append(0)
        print(on_bridge)
    return cnt


print(solution(2, 10, [7, 4, 5 , 6]))
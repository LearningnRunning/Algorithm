from collections import deque
def solution(bridge_length, weight, truck_weights):
    truck_orderby_weight = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    total_weight = 0
    answer = 0

    while truck_orderby_weight:
        total_weight -= bridge.popleft()

        if total_weight + truck_orderby_weight[0] <= weight:
            first_one = truck_orderby_weight.popleft()
            total_weight += first_one
            bridge.append(first_one)

        else:
            bridge.append(0)

        answer += 1

    while total_weight:
        total_weight -= bridge.popleft()

        answer += 1

    return answer
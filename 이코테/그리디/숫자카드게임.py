def find_highest_lowest_value(N, M):
    max_min = 0
    for _ in range(N):
        row = list(map(int, input().split()))
        max_min = max(max_min, min(row))

    return max_min
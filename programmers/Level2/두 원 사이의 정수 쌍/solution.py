from math import pow, sqrt, floor, ceil

def solution(r1, r2):
    count_per_quadrant = 0
    for x in range(1, r2 + 1):
        max_y = floor(sqrt(pow(r2, 2) - pow(x, 2)))
        min_y = ceil(sqrt(pow(r1, 2) - pow(x, 2))) if r1 > x else 0
        count_per_quadrant += max_y - min_y + 1

    return count_per_quadrant * 4


# 시간복잡도
def solution(r1, r2):
    count = 0
    r1_squared = r1**2
    r2_squared = r2**2
    for x in range(-r2, r2 + 1):
        for y in range(-r2, r2 + 1):
            distance_squared = x**2 + y**2
            if r1_squared <= distance_squared <= r2_squared:
                count += 1
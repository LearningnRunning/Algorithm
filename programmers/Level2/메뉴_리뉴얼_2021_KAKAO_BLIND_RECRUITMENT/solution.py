def solution(r1, r2):
    count = 0
    for x in range(-r2, r2 + 1):
        for y in range(-r2, r2 + 1):
            distance_squared = x**2 + y**2
            if r1**2 <= distance_squared <= r2**2:
                count += 1
    return count

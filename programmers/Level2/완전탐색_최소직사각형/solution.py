def solution(sizes):
    answer = 0
    w, h = 0, 0
    for size in sorted(sizes, reverse=True):
        if w < max(size):
            w = max(size)
        if h < min(size):
            h = min(size)
    return w * h

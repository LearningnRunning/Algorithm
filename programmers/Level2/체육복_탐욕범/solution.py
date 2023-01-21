def solution(n, lost, reserve):
    n -= len(lost)
    for i in reserve:
        if i in lost:
            n += 1
            lost.remove(i)
        elif i+1 in lost:
            n += 1
            lost.remove(i+1)
        elif i-1 in lost:
            n += 1
            lost.remove(i-1)
    return n
def solution(x):
    tep = list(str(x))
    tep = sum(map(int,tep))
    if x % tep == 0:
        return True
    else:
        return False
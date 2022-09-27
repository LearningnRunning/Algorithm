def solution(n):
    tmp_lst = [0, 1]
    for i in range(n - 1):
        tmp_lst.append(sum(tmp_lst[-2:]) % 1234567)
    return tmp_lst[n]

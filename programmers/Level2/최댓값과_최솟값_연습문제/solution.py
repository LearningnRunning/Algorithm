def solution(s):
    tmp_lst = list(map(int, s.split()))
    answer = "{0} {1}".format(min(tmp_lst), max(tmp_lst))
    return answer

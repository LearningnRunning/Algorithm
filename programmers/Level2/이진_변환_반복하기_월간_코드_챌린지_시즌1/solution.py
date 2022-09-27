def tmp_cnt(s):
    s_cnt = s.count("0")
    s = s.replace("0", "")
    return s_cnt, len(s)


def solution(s):
    zero_cnt = 0
    bi_cnt = 0
    while True:
        if s == "1":
            break
        s_cnt, s_tmp = tmp_cnt(s)
        bi_cnt += 1
        zero_cnt += s_cnt
        s = bin(s_tmp)[2:]
    answer = [bi_cnt, zero_cnt]
    return answer

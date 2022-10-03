def solution(n, words):
    for i, e in enumerate(words):
        if i >= 1:  # out of index 방지

            # 번호 선언
            if (i + 1) % n == 0:
                p = n  # 딱 떨지면 인원수가 곧 그 사람의 번호
            else:
                p = (i + 1) % n  # 인원수의 나머지가 번호

            if e[0] != words[i - 1][-1]:  # 끝말잇기를 성공하면
                return [p, (i // n) + 1]
            elif e in words[:i]:  # 앞에서 한 단어라면
                return [p, (i // n) + 1]

    return [0, 0]  # 다 통과했을 경우

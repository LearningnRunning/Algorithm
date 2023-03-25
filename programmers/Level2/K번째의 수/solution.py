def solution(a, c):
    answer = []
    for i in c:
        tep = a[i[0]-1:i[1]]
        tep.sort()
        answer.append(tep[i[2]-1])
    return answer
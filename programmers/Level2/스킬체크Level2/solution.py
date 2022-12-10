def solution(record):
    answer = []
    name = {}
    for v in record:
        v = v.split(" ")
        if v[0] == "Enter":
            name[v[1]] = v[2]
            answer.append("{}님이 들어왔습니다.".format(v[1]))
        elif v[0] == "Change":
            name[v[1]] = v[2]
        elif v[0] == "Leave":
            answer.append("{}님이 나갔습니다.".format(v[1]))

    answer = [n.replace(n.split("님이")[0], name[n.split("님이")[0]]) for n in answer]
    return answer


record = [
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan",
]
solution(record)

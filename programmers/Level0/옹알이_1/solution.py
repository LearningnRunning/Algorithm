def solution(babbling):
    answer = 0
    for b in babbling:
        for old, new in replace_dict.items():
            b = b.replace(old, new) 
        if b.isdigit():
            answer += 1 

    return answer

replace_dict = {
    "aya": "1",
    "ye": "2",
    "woo": "3",
    "ma": "4"
}

# str.isdigit() 힌트를 얻고 숫자로 모두 바꿔 숫자인지 아닌지로 판단하는 알고리즘을 짰으나, 딕셔너리도 필요 없이 공백으로 만들어 처리하면 더 간단했다
def solution(babbling):
    answer = 0
    for b in babbling:
        for old in ["aya", "ye", "woo", "ma"]:
            b = b.replace(old, "") 
        if not bool(b):
            answer += 1 
    return answer
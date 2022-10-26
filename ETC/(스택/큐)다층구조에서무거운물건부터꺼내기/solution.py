def solution(stack1, stack2, stack3):
    tmp = []
    answer = ""
    # 튜플에서 뒤쪽을 층수로 앞쪽을 벨류 값으로 해야 max() 할 때에 벨류값들을 비교해서 산출해준다.
    if stack1:
        tmp += [(i, 1) for i in stack1]
    if stack2:
        tmp += [(i, 2) for i in stack2]
    if stack3:
        tmp += [(i, 3) for i in stack3]
    while tmp:
        answer += str(tmp.pop(tmp.index(max(tmp)))[1])  # max() 값을 pop 하면서 해당 층을 저장
    return answer

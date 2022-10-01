def solution(n):
    tmp = bin(n)[2:].count("1")
    while True:
        n += 1
        if tmp == bin(n)[2:].count("1"):
            answer = n
            break
    return answer

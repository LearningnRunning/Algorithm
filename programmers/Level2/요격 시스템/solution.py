def solution(targets):
    answer, defense = 0, 100_000_001
    for start, end in sorted(targets, reverse=True):
        if end <= defense: 
            defense = start + .5
            answer += 1
    return answer
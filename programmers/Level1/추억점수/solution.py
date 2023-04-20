from collections import Counter
def solution(name, yearning, photo):
    answer = []
    score_dict = {n:y for n,y in zip(name, yearning)}
    for p in photo:
        total_score = 0
        p_c = Counter(p)
        for k,v in p_c.items():
            if k in score_dict.keys():
                total_score += score_dict[k] * v
        answer.append(total_score)
    
    return answer
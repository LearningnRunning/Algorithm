def solution(storey):
    ans = 0
    i = 0
    while storey > 0:
        tmp3 = 10**i # 해당 자릿수 
        tmp = storey%(10**(i+1)) # 해당 자릿수의 숫자
        tmp2 = 5*(tmp3) # 
        if tmp <= tmp2:
            tmp1 = tmp/(tmp3) # 마법의 돌 개수
            ans += int(tmp1)
            if storey%(10**(i+2)) >= 5*(tmp3+1):
                storey = round(storey,-i-1) # 남은 층 수 계산( 자릿수에서 반절 이상이면 반올림)
            else:
                storey -= tmp # 아래면 버림 
        else:
            ans += int((10**(i+1)-tmp)/tmp3)
            storey = round(storey,-i-1)
        i += 1
    return ans


# 다른 사람 풀이
def solution1(storey):
    if storey < 10 :
        return min(storey, 11 - storey)
    left = storey % 10
    return min(left + solution(storey // 10), 10 - left + solution(storey // 10 + 1))



storey = 5555 # 18
solution(storey)
solution1(storey)
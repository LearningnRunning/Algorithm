def solution(food):
    ans = ''
    for i,v in enumerate(food[1:]):
        # 1 이상인 값만
        if v > 1:
            # 몫만 곱하기
            ans += str(i+1)*(v//2)
    # 중간에 물 놓고 거꾸로 바꾼 음식 붙이긴
    return ans + "0"+ans[::-1]

food = [1, 3, 4, 6]
solution(food)
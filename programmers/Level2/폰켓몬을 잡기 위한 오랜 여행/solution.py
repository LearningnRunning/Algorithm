def solution(nums):
    answer = len(set(nums))
    if int(len(nums) / 2) < len(set(nums)):
        answer = int(len(nums) / 2)
    return answer


# 중복없는 번호 종류의 개수가 최댓값
# 고를 수 잆는 수가 번호 종류보다 적으면 그것이 최댓값

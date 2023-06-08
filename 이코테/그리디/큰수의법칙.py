def construct_largest_number(lst, N, M, K):
    lst.sort(reverse=True)
    max_num = lst[0]
    quotient = M // (K+1)
    answer = 0
    answer += (M % (K+1)) * max_num
    print(answer)
    answer += lst[1] * quotient
    print(answer)

    answer += max_num * K * quotient

    return answer

lst = [3,4,3,4,3]
N = len(lst)
M = 7
K = 2

# lst = [2, 4, 5, 4, 6]
# N = 5
# M = 8
# K = 3
print(construct_largest_number(lst, N, M, K))


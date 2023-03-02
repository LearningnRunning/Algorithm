# solution1
def solution(my_string):
    tmp_lst = my_string.split(' ')
    ans = 0
    for i, v in enumerate(tmp_lst):
        if i == 0:
            ans += int(v)
        elif i%2 == 0:
            v = int(v)
            if tmp_lst[i-1] == '+':
                ans += v
            else:
                ans -= v
    return ans

# solution2
solution=eval



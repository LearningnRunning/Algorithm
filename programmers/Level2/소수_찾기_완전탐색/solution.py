from itertools import permutations
def solution(numbers):
    a = list(numbers)
    a.sort(reverse=True)
    n = int(''.join(a))
    if n < 2:
        return []
    s = [0, 0] + [1] * (n - 1)
    for i in range(2, int(n**.5)+1):
        if s[i]:
            s[i*2::i] = [0] * ((n - i)//i)
    tmp = [i for i, v in enumerate(s) if v]
    num = []
    for j in range(1, len(numbers)+1):
      num = num + list(map(''.join, permutations(a, j)))
    num = list(map(int,num))
    return len(set(num) & set(tmp))
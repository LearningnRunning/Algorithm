def solution(number, k):
    num_digits = list(number)
    result = []

    for digit in num_digits:
        while k > 0 and result and result[-1] < digit:
            result.pop()
            k -= 1
        result.append(digit)

    # If k is not exhausted, remove remaining digits from the end
    result = result[:-k] if k > 0 else result

    return ''.join(result)

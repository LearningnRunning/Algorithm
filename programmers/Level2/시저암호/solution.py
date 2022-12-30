def solution(s, n):
        answer = []
        for i in s:
            if ord(i) == 32: #공백문자
                answer.append(i)
            elif ord(i) >= 119 or 87 <= ord(i) <= 90 :
                answer.append(chr(ord(i)+n-26))
            else:
                answer.append(chr(ord(i)+n))
        return ''.join(answer)
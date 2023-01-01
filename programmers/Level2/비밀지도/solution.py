def solution(n, arr1, arr2):
    answer =[]
    tmp = []
    for i,j in zip(arr1,arr2):
        i = bin(i)[2:].zfill(n) #zero를 채워주는 zfill(자릿수)
        j = bin(j)[2:].zfill(n)
        for m in range(n):
            if i[m] == '1' or j[m] == '1':
                tmp.append('#')
            else:
                tmp.append(' ')
        answer.append(''.join(tmp))
        tmp.clear()
    return answer
def solution(elements):
    result = set()
    elementLen = len(elements)
    elements *= 2
    print(elements)
    for i in range(elementLen):
        for j in range(elementLen):
            result.add(sum(elements[j:j+i+1]))
    return len(result)
elements = [7,9,1,1,4]
solution(elements)
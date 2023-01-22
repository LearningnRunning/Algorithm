def solution(p):
    n = p
    while p.find('()') != -1:
      p = p[0 : p.find('()') : ] + p[p.find('()') + 2 : :]
    if len(p) == 0:
      answer = n
    else:
      b = p
      p = list(p)
      for i in range(len(p)):
        if p[i] == ')':
          p[i] = '('
        else:
          p[i] = ')'
      print(p)
      p = ''.join(p)
      answer =  n[0 : n.find(b) : ] + p + n[n.find(b) + len(p) : :]
    return answer
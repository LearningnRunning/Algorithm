from collections import deque
def solution(priorities, location):
  answer = 1
  deq_lst = deque()
  for i,j in zip(range(len(priorities)),priorities):
    deq_lst.append([j,i])
  print(deq_lst)

  while deq_lst:
    if deq_lst[0][0] == max(deq_lst)[0]:
        if deq_lst[0][1] == location:
          return answer
        else:
          deq_lst.popleft()
          answer +=1
        
    else:
      deq_lst.rotate(-1)
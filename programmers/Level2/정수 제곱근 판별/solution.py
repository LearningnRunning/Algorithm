from math import *
def solution(n):
    n = sqrt(n)
    if n%1 == 0: return int(pow(n+1,2))
    else: return -1
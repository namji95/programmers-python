def solution(p, m, c):
    result = sum([p*i for i in range(1, c+1)]) - m
    return result if result > 0 else 0
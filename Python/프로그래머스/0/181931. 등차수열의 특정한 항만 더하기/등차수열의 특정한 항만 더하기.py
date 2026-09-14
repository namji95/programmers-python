def solution(a, d, included):
    return sum(a + (d * i) for i, k in enumerate(included) if k)
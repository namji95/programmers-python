def solution(a, b):
    r = []
    for idx in range(len(a)):
        r.append(a[idx] * b[idx])
    return sum(r)
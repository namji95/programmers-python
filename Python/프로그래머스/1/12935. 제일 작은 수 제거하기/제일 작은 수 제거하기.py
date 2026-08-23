def solution(a):
    a.remove((sorted(a)[:1] if a else [-1])[0])
    return a if a else [-1]
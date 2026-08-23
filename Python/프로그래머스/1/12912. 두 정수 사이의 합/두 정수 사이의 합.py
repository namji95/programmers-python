def solution(a, b):
    if a > b:
        max = a
        min = b
    else:
        max = b
        min = a
    return sum([i for i in range(min, max+1)])
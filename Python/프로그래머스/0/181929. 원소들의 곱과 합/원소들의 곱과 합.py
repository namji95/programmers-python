def solution(n):
    from functools import reduce

    return 1 if reduce(lambda x, y: x * y, n) < sum(n) ** 2 else 0
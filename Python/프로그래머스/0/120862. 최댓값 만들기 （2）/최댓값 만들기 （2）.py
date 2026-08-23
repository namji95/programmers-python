def solution(n):
    import math
    from itertools import combinations
    return max(map(lambda x: math.prod(x), combinations(n, 2)))
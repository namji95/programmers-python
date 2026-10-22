def solution(balls, share):
    from math import factorial as f

    n = f(balls)
    n_minus_m = f(balls - share)
    m = f(share)

    return n // (n_minus_m * m)
import math


def solution(n, m):
    lcm = n * m // math.gcd(n, m)
    return [math.gcd(n, m), lcm]
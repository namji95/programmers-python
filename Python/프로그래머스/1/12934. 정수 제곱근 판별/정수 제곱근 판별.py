import math

def solution(n):
    sqrt_n = str(math.sqrt(n))[-1:]
    if sqrt_n == "0":
        return int(math.pow(int(math.sqrt(n))+1, 2))
    else:
        return -1
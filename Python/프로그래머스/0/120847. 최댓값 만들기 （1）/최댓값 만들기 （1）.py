def solution(numbers):
    m = sorted(numbers, reverse=True)
    return m[0] * m[1]
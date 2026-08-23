def solution(order):
    return sum([1 for i in str(order) if i in ("3", "6", "9")])
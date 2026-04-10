def solution(a, b):
    return int(f"{a}{b}" if int(f"{a}{b}") > int(f"{b}{a}") else f"{b}{a}")
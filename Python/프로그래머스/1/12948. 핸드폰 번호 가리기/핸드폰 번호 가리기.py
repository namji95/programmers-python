def solution(p):
    length = len(p)-4
    lst = list(p)
    for  idx, s in enumerate(lst):
        if idx == length:
            break
        lst[idx] = "*"
    return "".join(lst)
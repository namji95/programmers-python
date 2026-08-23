def solution(a1, a2):
    if len(a1) == len(a2):
        return -1 if sum(a1) < sum(a2) else 1 if sum(a1) > sum(a2) else 0
    else:
        return -1 if len(a1) < len(a2) else 1
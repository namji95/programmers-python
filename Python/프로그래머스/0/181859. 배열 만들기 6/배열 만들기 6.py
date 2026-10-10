def solution(arr):
    stk = []
    for i, a in enumerate(arr):
        if len(stk) == 0:
            stk.append(a)
            continue
        if a == stk[len(stk) - 1]:
            stk.pop()
            continue
        if a != stk[len(stk) - 1]:
            stk.append(a)
    if len(stk) == 0:
        return [-1]
    return stk
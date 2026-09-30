def solution(s):
    sort = sorted(s)
    d = {}
    for ss in sort:
        if ss not in d:
            d[ss] = 1
        else:
            d[ss] += 1
    return ''.join(k for k in d if d[k] == 1)
def solution(sizes):
    for i in sizes:
        i.sort(reverse=True)
    f = 0
    s = 0
    for i in sizes:
        f = max(f, i[0])
        s = max(s, i[1])
    return f * s
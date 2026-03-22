def solution(c1, c2, g):
    for s in g:
        if s in c1:
            if s == c1[0]:
                c1.remove(s)
            else:
                return "No"
        elif s in c2:
            if s == c2[0]:
                c2.remove(s)
            else:
                return "No"
        else:
            return "No"
    return "Yes"
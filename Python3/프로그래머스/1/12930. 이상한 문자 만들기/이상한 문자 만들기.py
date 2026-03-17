def solution(s):
    l = s.split(' ')
    for c in l:
        new_c = list(c)
        for i in range(len(c)):
            if i % 2 == 0:
                new_c[i] = new_c[i].upper()
            else:
                new_c[i] = new_c[i].lower()
        l[l.index(c)] = ''.join(new_c)

    return ' '.join(l)
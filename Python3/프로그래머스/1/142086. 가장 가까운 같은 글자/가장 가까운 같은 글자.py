def solution(s):
    a = []
    di = {}
    for i in range(len(s)):
        if s[i] not in di:
            a.append(-1)
        else:
            a.append(i - di[s[i]])
        di[s[i]] = i
    return a
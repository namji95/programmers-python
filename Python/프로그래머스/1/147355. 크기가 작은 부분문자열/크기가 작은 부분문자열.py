def solution(t, p):
    cnt = 0
    for i in range(0, len(t)):
        if t[i:i+len(p)] <= p and len(t[i:i+len(p)]) == len(p):
            cnt += 1
    return cnt
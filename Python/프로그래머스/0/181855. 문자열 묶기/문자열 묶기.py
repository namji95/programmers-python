def solution(strArr):
    cnt = {}
    for s in strArr:
        cnt[len(s)] = cnt.get(len(s), 0) + 1
    return max(cnt.values())
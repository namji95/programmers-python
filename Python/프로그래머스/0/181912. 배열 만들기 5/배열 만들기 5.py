def solution(intStrs, k, s, l):
    return [int(intStrs[i][s:s + l]) for i in range(len(intStrs)) if int(intStrs[i][s:s + l]) > k]
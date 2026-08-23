def solution(num, k):
    for i, s in enumerate(str(num)):
        if s == str(k):
            return i + 1
    return -1
def solution(d, budget):
    d.sort()
    cnt = 0
    total = 0
    for i in d:
        if total + i <= budget:
            total += i
            cnt += 1
    return cnt
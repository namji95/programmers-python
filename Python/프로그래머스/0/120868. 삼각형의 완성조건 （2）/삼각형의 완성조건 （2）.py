def solution(sides):
    cnt = 0
    for i in range(1, sum(sides)):
        if max(sides) < i < sum(sides):
            cnt += 1
        elif (min(sides) + i) > max(sides):
            cnt += 1
    return cnt
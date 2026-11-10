def solution(num, total):
    d = 0
    for i in range(1, num):
        d += i
    start = (total - d) // num
    return [i for i in range(start, start + num)]
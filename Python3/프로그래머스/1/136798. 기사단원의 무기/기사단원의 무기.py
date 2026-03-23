def solution(n, l, p):
    divisor = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            divisor[j] += 1

    a = 0
    for i in divisor:
        if i <= l:
            a += i
        else:
            a += p
    return a
def solution(n):
    cnt = 0
    while True:
        if n == 1:
            break
        cnt += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        if n == 1:
            break
        if cnt == 500:
            break

    return cnt if cnt < 500 else -1
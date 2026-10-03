def solution(n):
    answer = 1
    while n > answer:
        n //= answer
        answer += 1

    if n == answer:
        return answer
    else:
        return answer - 1
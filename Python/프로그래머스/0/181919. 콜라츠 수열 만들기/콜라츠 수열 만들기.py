def solution(n):
    answer = [n]
    while answer[-1] != 1:
        answer.append(answer[-1] // 2 if answer[-1] % 2 == 0 else 3 * answer[-1] + 1)
    return answer
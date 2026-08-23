def solution(a1, a2):
    answer = [[0] * len(a1[0]) for _ in range(len(a1))]

    for index, (i, j) in enumerate(zip(a1, a2)):
        for idx, (k, m) in enumerate(zip(i, j)):
            answer[index][idx] = k + m

    return answer
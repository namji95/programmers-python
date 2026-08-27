def solution(names):
    answer = []
    if len(names) == 5:
        return [names[0]]
    answer.append(names[0])
    for i, name in enumerate(names):
        if (i + 1) == len(names):
            return answer
        if (i + 1) % 5 == 0:
            answer.append(names[i + 1])

    return answer
def solution(numlist, n):
    answer = []

    if n in numlist:
        answer.append(n)

    distance = 1
    while len(answer) < len(numlist):
        if n + distance in numlist:
            answer.append(n + distance)

        if n - distance in numlist:
            answer.append(n - distance)

        distance += 1

    return answer
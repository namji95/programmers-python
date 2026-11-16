def solution(lines):
    counts = {}

    for start, end in lines:
        for x in range(start, end):
            if x not in counts:
                counts[x] = 0
            counts[x] += 1

    answer = 0

    for count in counts.values():
        if count >= 2:
            answer += 1

    return answer
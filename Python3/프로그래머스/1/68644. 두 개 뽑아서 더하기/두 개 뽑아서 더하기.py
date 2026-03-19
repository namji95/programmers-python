def solution(numbers):
    a = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] in a: continue
            a.append(numbers[i] + numbers[j])

    return sorted(a)
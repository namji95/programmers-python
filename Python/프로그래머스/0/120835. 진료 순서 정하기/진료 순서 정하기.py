def solution(emergency):
    answer = [0] * len(emergency)
    for _ in range(len(emergency)):
        answer[emergency.index(max(emergency))] = max(answer) + 1
        emergency[emergency.index(max(emergency))] = 0
    return answer
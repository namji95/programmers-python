def solution(numLog):
    switch = {1: "w", -1: "s", 10: "d", -10: "a"}
    return "".join([switch[numLog[i] - numLog[i - 1]] for i in range(1, len(numLog))])
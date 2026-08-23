def solution(a):
    temp = -1
    answer = []
    for i in a:
        if temp != i:
            answer.append(i)
            temp = i
    return answer
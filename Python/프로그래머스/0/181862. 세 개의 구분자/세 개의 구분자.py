def solution(myStr):
    answer = []
    for s in myStr.replace("a", ",").replace("b", ",").replace("c", ",").split(","):
        if s:
            answer.append(s)
    return answer if answer else ["EMPTY"]
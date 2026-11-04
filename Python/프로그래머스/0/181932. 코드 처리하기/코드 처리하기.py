def solution(code):
    answer = ""
    mode = 0
    for i, c in enumerate(code):
        if c == "1":
            if mode == 0:
                mode = 1
            else:
                mode = 0
            continue
        if mode == 0 and i % 2 == 0:
            answer += c
        elif mode == 1 and i % 2 != 0:
            answer += c
    return answer if answer else "EMPTY"
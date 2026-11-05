def solution(polynomial):
    answer = []
    p = polynomial.split(' + ')
    x = 0
    i = 0
    for x_str in p:
        if 'x' in x_str:
            x_split = x_str.split('x')
            x += int(x_split[0] if x_split[0] != '' else 1)
        else:
            i += int(x_str)

    if x == 1:
        answer.append("x")
    elif x > 1:
        answer.append(f"{x}x")

    # 상수항이 있으면 마지막에 추가한다.
    if i:
        answer.append(str(i))

    return " + ".join(answer)
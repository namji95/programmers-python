def solution(food):
    a = ''
    for idx, i in enumerate(food):
        if idx == 0:
            continue
        a += f"{idx}"*(i//2)
    r = ''.join(reversed(a))
    return f"{a}0{r}"
def solution(k, score):
    top_three = []
    bottom = []

    for i in score:
        top_three.sort(reverse=True)
        
        if len(top_three) < k:
            top_three.append(i)

        elif top_three[-1] < i:
            top_three.pop()
            top_three.append(i)

        bottom.append(min(top_three))

    return bottom
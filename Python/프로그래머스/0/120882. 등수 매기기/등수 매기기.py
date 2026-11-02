def solution(score):
    answer = []
    new_score = sorted([sum(s) / 2 for s in score], reverse=True)
    print(new_score)

    for s in score:
        answer.append(new_score.index(sum(s) / 2) + 1)

    return answer
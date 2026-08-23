def solution(k, m, score):
    # 점수가 높은 사과부터 쓰는 게 유리
    # → 내림차순 정렬
    score.sort(reverse=True)

    answer = 0

    # m개씩 끊어서 상자 만들기
    for i in range(0, len(score), m):

        # 상자 하나 만들 수 있는지 확인
        if i + m > len(score):
            break  # 남은 사과가 m개 미만이면 버림

        # 해당 상자의 최소값은 "마지막 값"
        # (내림차순이므로)
        min_value = score[i + m - 1]

        # 상자 가격 = 최소값 * m
        answer += min_value * m

    return answer
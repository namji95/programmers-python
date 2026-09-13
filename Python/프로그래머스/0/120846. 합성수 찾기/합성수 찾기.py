def solution(n):
    output = 0  # 합성수의 개수를 저장할 변수
    for i in range(4, n + 1):  # 4부터 시작하는 이유는 1, 2, 3은 합성수가 아니기 때문
        for j in range(2, int(i ** 0.5) + 1):  # 약수를 찾기 위해 제곱근까지만 확인
            if i % j == 0:  # j가 i의 약수라면
                output += 1  # 합성수 카운트 증가
                break  # 더 이상의 약수 검사는 필요 없음
    return output  # 합성수의 총 개수 반환
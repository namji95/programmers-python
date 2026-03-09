def solution(num):
    answer = ''
    if num == 0:
        return "Even"
    if num % 2 == 0:
        answer = 'Even'
    else:
        answer = 'Odd'
    return answer
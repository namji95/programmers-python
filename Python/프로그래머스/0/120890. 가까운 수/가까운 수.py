def solution(array, n):
    array = sorted(array)
    answer = array[0]
    for number in array:
        if abs(number - n) < abs(answer - n):
            answer = number
    return answer
def solution(numbers, num1, num2):
    return numbers[num1:num2+1 if num2+1 < len(numbers) else len(numbers)]
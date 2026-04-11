def solution(n):
    odd_or_even = 2 if n % 2 == 0 else 1
    sum = 0
    for i in range(odd_or_even, n + 1, 2):
        if odd_or_even == 1:
            sum += i
        else:
            sum += i ** 2

    return sum
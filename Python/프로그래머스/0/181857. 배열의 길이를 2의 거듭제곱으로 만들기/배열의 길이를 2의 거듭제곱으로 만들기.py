def solution(arr):
    if len(arr) < 2:
        return arr
    
    total_length = 1
    while True:
        total_length *= 2
        if total_length >= len(arr):
            break

    return arr + [0] * (total_length - len(arr))
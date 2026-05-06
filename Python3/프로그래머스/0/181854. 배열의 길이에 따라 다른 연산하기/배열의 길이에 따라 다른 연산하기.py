def solution(arr, n):
    target = 1 if len(arr) % 2 == 0 else 0

    for idx in range(len(arr)):
        if idx % 2 == target:
            arr[idx] += n

    return arr
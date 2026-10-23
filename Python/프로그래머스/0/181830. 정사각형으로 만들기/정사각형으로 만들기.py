def solution(arr):
    row = len(arr)
    col = len(arr[0])
    if row > col:
        for idx, i in enumerate(arr):
            arr[idx].extend([0] * (row - col))
    else:
        for _ in range(col - row):
            arr.append([0] * col)
    return arr
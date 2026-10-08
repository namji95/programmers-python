def solution(arr):
    for i in range(len(arr)):
        before_arr = arr.copy()
        for j in range(len(arr)):
            if arr[j] >= 50 and arr[j] % 2 == 0:
                arr[j] //= 2
            elif arr[j] < 50 and arr[j] % 2 != 0:
                arr[j] = arr[j] * 2 + 1
            else:
                continue
        if before_arr == arr:
            return i
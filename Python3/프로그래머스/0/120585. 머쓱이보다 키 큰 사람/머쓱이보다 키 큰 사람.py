def solution(array, height):
    cnt = 0
    array.append(height)
    array.sort()
    for i in array:
        if i > height:
            cnt += 1

    return cnt
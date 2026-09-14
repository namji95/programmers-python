def solution(arr, flag):
    answer = []
    for i, k in enumerate(flag):
        if k:
            for _ in range(arr[i] * 2):
                answer.append(arr[i])
        else:
            answer = answer[:-arr[i]]
            
    return answer
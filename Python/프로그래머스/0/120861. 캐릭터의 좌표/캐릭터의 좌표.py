def solution(keyinput, board):
    answer = [0, 0]
    for k in keyinput:
        if k == 'up':
            answer[1] += 1
            if board[1] // 2 < answer[1]:
                answer[1] -= 1
        elif k == 'down':
            answer[1] -= 1
            if -(board[1] // 2) > answer[1]:
                answer[1] += 1
        elif k == 'left':
            answer[0] -= 1
            if -(board[0] // 2) > answer[0]:
                answer[0] += 1
        elif k == 'right':
            answer[0] += 1
            if board[0] // 2 < answer[0]:
                answer[0] -= 1

    return answer
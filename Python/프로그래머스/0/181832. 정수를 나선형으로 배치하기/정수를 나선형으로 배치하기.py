def solution(n):
    board = [[0] * n for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction = 0
    row, col = 0, 0
    
    for num in range(1, n * n + 1):
        board[row][col] = num
        
        if num == n * n:
            break
            
        next_row = row + directions[direction][0]
        next_col = col + directions[direction][1]

        if not (0 <= next_row < n and 0 <= next_col < n) or board[next_row][next_col] != 0:
            direction = (direction + 1) % 4
            next_row = row + directions[direction][0]
            next_col = col + directions[direction][1]
            
        row, col = next_row, next_col

    return board
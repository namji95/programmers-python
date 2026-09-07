def solution(my_string, m, c):
    return ''.join([my_string[i::m] for i in range(m)][c - 1])
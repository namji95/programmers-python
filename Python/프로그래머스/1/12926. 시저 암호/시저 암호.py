def solution(s, n):
    answer = ''
    for c in s:
        if c == ' ':
            answer += ' '
        elif c.islower():
            answer += chr((ord(c) - ord('a') + n) % 26 + ord('a'))
        else:
            answer += chr((ord(c) - ord('A') + n) % 26 + ord('A'))

    return answer
def solution(cipher, code):
    return ''.join(c for i, c in enumerate(cipher, start=1) if i % code == 0)
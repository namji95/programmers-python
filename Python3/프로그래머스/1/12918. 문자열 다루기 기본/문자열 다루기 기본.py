import re

def solution(s):
    l = len(s)
    return bool(re.match(r"^\d+$", s) and (l == 4 or l == 6))
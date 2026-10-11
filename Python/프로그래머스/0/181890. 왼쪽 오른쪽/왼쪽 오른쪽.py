def solution(str_list):
    for i, s in enumerate(str_list):
        if "l" == s:
            return str_list[:i]
        if "r" == s:
            return str_list[i + 1:]
    return []
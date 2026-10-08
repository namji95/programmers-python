def solution(s):
    answer = 0
    split_s = s.split()
    for idx, i in enumerate(split_s):
        if i != "Z":
            answer += int(i)
        else:
            answer -= int(split_s[idx - 1])
    return answer
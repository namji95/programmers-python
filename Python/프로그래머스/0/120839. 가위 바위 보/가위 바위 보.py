def solution(rsp):
    r = ""
    for s in rsp:
        if s == "2":
            r += "0"
        elif s == "0":
            r += "5"
        else:
            r += "2"
    return r
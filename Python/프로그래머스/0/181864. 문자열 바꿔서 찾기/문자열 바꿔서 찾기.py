def solution(myString, pat):
    translate_a_b = ""
    for s in myString:
        if s == "A":
            translate_a_b += "B"
        elif s == "B":
            translate_a_b += "A"
    return 1 if pat in translate_a_b else 0
def solution(str):
    p_n_y = {
        "p": 0,
        "y": 0
    }
    for s in str:
        if s.lower() not in ("p", "y"):
            continue

        p_n_y[s.lower()] += 1

    return True if p_n_y["p"] == p_n_y["y"] else False
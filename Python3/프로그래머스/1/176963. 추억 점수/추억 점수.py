def solution(n, y, p):
    name_dict = {}
    for idx, name in enumerate(n):
        name_dict[name] = y[idx]

    photo_list = []
    for idx, photo in enumerate(p):
        scored = 0
        for name in photo:
            if name in name_dict:
                scored += name_dict[name]
        photo_list.append(scored)
        
    return photo_list
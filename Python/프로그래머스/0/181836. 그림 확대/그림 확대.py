def solution(picture, k):
    answer = []
    new_picture = []
    for pic in picture:
        for i in range(k):
            new_picture.append(pic)
    for pic in new_picture:
        pic_str = ""
        for s in pic:
            pic_str += s * k
        answer.append(pic_str)
    return answer
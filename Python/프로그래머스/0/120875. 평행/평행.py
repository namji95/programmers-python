def solution(dots):
    a, b, c, d = dots
    
    def is_parallel(p1, p2, p3, p4):
        dx1 = p2[0] - p1[0]
        dy1 = p2[1] - p1[1]
        dx2 = p4[0] - p3[0]
        dy2 = p4[1] - p3[1]

        return dy1 * dx2 == dy2 * dx1

    if is_parallel(a, b, c, d):
        return 1

    if is_parallel(a, c, b, d):
        return 1

    if is_parallel(a, d, b, c):
        return 1

    return 0
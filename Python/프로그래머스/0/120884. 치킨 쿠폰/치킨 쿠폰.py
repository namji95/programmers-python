def coupon(chicken):
    if chicken < 10:
        return 0
    service = chicken // 10
    remaining = chicken % 10 + service
    return service + coupon(remaining)


def solution(chicken):
    return coupon(chicken)
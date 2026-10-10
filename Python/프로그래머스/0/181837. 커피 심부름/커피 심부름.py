def solution(order):
    return sum([5000 if o.endswith('cafelatte') or o.startswith('cafelatte') else 4500 for o in order])
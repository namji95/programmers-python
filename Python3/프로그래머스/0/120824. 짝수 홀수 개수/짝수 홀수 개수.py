def solution(num_list):
    return [sum(map(lambda x: 1 if x % 2 == 0 else 0, num_list)), sum(map(lambda x: 1 if x % 2 != 0 else 0, num_list))]
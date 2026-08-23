def solution(num_list):
    even_str = ''
    odd_str = ''
    for i in num_list:
        if i % 2 == 0:
            even_str += str(i)
        else:
            odd_str += str(i)

    return int(even_str) + int(odd_str)
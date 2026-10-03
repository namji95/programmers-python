def solution(my_string):
    new_string = ""
    for s in my_string:
        if s.isdigit():
            new_string += s
        else:
            new_string += ","
    split_string = new_string.split(",")
    return sum(int(s) for s in split_string if s)
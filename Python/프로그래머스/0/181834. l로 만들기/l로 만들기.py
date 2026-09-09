def solution(myString):
    return ''.join(['l' if myString[i] < 'l' else myString[i] for i in range(len(myString))])
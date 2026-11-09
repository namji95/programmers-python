def solution(array):
    from collections import Counter
    
    common = Counter(array).most_common(2)
    
    if len(common) == 1:
        return common[0][0]
    
    if common[0][1] == common[1][1]:
        return -1
    
    return common[0][0]
def solution(n, arr1, arr2):
    answer = []
    for ar1, ar2 in zip(arr1, arr2):
        a1 = format(ar1, 'b').zfill(n)
        a2 = format(ar2, 'b').zfill(n)
        
        s = ''
        for i, j in zip(a1, a2):
            if i == j:
                if i == '1':
                    s += '#'
                else:
                    s += ' '
            else:
                s += '#'
                
        answer.append(s)
    return answer
def solution(x, n):
    y = [x];
    for i in range(1,n):
        y= y + [x+x*(i)]
    return(y)
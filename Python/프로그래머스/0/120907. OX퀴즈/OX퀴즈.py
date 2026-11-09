def solution(quiz):
    answer = []
    
    for q in quiz:
        split_quiz = q.split(" = ")
        if str(eval(split_quiz[0])) == split_quiz[1]:
            answer.append("O")
        else:
            answer.append("X")
            
    return answer
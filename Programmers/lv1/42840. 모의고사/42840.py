def solution(answers):
    answer = []
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    
    def check(p: list) -> int:  
        p_answer = []
        for i in range(len(answers)):
            j = i
            if i > len(p)-1:
                j = i % len(p)
                
            if p[j] == answers[i]:
                p_answer.append(1)
            else:
                p_answer.append(0)
        return sum(p_answer)
    
    score = []
    score.append(check(p1))
    score.append(check(p2))
    score.append(check(p3))
    print(score)
    
    count = score.count(max(score))
    
    if count == 1:
        answer.append(score.index(max(score))+1)
    
    if count == 3:
        return [1,2,3]
    
    if count == 2:
        for i in range(3):
            if score[i] == max(score):
                answer.append(i+1)

    return answer
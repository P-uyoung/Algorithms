import re

def solution(dartResult):
    answer = []
    bonus_dic = {'S':1, 'D':2, 'T':3}
    pattern = '(\d+)([SDT])([*#]?)'
    dart = re.findall(pattern, dartResult)
    for i in range(3):
        answer.append(int(dart[i][0])**bonus_dic[dart[i][1]])
        if dart[i][2] == '*':
            answer[i] = answer[i]*2
            if i != 0:
                answer[i-1] = answer[i-1]*2
        elif dart[i][2] == '#':
            answer[i] = -answer[i]
    
    return sum(answer)
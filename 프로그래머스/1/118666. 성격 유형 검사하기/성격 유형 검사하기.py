def solution(survey, choices):
    personal = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for types, score in zip(survey, choices):
        if score <= 3:
            personal[types[0]] += (4-score)
        elif score >=5:
            personal[types[1]] += score-4
    
    ans = ''
    if personal['R'] >= personal['T']:
        ans += 'R'
    else: ans += 'T'
    
    if personal['C'] >= personal['F']:
        ans += 'C'
    else: ans += 'F'
    
    if personal['J'] >= personal['M']:
        ans += 'J'
    else: ans += 'M'
    
    if personal['A'] >= personal['N']:
        ans += 'A'
    else: ans += 'N'
            
    return ans
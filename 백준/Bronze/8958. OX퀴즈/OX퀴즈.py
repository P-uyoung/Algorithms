n = int(input())

def quiz(s):
    score, res = 0, 0
    for i in s:
        if i == 'O':
            score += 1
        else:
            score = 0
        res += score
    return res

for _ in range(n):
    print(quiz(input()))
        
    
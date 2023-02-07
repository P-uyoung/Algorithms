from itertools import permutations
import math

def solution(numbers):
    answer = 0
    cand = set()
    root = 0
    n = len(numbers)
    
    temp = ''
    for i in range(n):
        temp += '0'
    if temp == numbers:
        return 0
    
    # 일의 자리
    prime = [2,3,5,7]
    one = set(numbers)
    for i in one:
        if int(i) in prime:
            answer += 1
    
    # 2이상
    for k in range(2,n+1):
        permu = list(permutations(numbers, k))
        for i in range(len(permu)):
            temp = ''
            for j in range(k):
                if permu[i][0] == '0':
                    break
                temp += permu[i][j]
            if temp != '':
                cand.add(int(temp))
    
    for num in cand:
        root = math.sqrt(num)
        check = 'true'
        for j in range(2, math.floor(root)+1):
            if num % j == 0:
                check = 'fail'
                break
        if check == 'true':
            answer += 1
            
    return answer
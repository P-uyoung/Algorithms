from itertools import combinations

def solution(brown, yellow):
    prime = []
    d = 2
    
    x = yellow
    while d <=x:
        if x % d == 0:
           x = x/d
           prime.append(d)
        else:
            d += 1
    
    b = set()
    for k in range(1,int(len(prime)/2)+1):
        combn = list(combinations(prime, k))
        for i in range(len(combn)):
            temp = 1
            for j in range(k):
                temp *= combn[i][j]
            b.add(temp)
    b.add(1)
    b = list(b)
    a = []
    for i in b:
        a.append(int(yellow/i))
        
    for i in range(len(b)):
        if brown == (b[i]*2+a[i]*2+4):
            if b[i] <= a[i]:
                return [a[i]+2, b[i]+2]
            else:
                return [b[i]+2, a[i]+2]
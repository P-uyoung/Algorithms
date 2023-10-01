# https://school.programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    arr = []
    for a in ['A', 'E', 'I', 'O', 'U']:
        arr.append(a)
    
    load = arr
    for i in range(4):
        tmp = []
        for a in load:
            for b in ['A', 'E', 'I', 'O', 'U']:
                tmp.append(a+b)
        load = tmp
        arr += load
    # print(arr)    
    arr.sort()
    
    return arr.index(word)+1
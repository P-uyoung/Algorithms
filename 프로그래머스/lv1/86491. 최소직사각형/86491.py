def solution(sizes):
    max_0 = 0
    for i in range(len(sizes)):
        if sizes[i][0] > max_0:
            max_0 = sizes[i][0]
    # print(max_0)
            
        
    max_1 = 0 
    for i in range(len(sizes)):
        if sizes[i][1] > max_1:
            max_1 = sizes[i][1]
    # print(max_1)
    
    second = []
    for i in range(len(sizes)):
        second.append(min(sizes[i]))
    
    if max_0 >= max_1:
        return max_0 * max(second)
    else:
        return max_1 * max(second)
        
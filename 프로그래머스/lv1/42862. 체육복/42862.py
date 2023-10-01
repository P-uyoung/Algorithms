def solution(n, lost, reserve):
    
    net_lost = list(set(lost)-set(reserve))
    net_reserve = list(set(reserve)-set(lost))
    lost=net_lost
    reserve=net_reserve
    count=n-len(lost)
    
    # lost = sorted(lost)
    # reserve = sorted(reserve)
    while len(lost)!=0:
        a = lost.pop()
        
        if a+1 in reserve:
            i = reserve.index(a+1)
            reserve.pop(i)
            count +=1

        elif a-1 in reserve:
            i = reserve.index(a-1)
            reserve.pop(i)
            count +=1  
        
    return count
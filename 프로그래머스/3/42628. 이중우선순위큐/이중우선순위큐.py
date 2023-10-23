from heapq import heappush, heappop

def solution(operations):
    min_heap, max_heap = [], []
    for opr in operations:
        let, num = opr.split()
        if let == 'I':
            heappush(min_heap, int(num))
            heappush(max_heap, -int(num))
            
        elif let == 'D':
            if not max_heap: 
                pass
            elif num == '1':
                d = heappop(max_heap)
                min_heap.remove(-d)
            else:
                d = heappop(min_heap)
                max_heap.remove(-d)           
        
    if not min_heap:
        ans = [0,0]
    else: 
        ans = [max(min_heap), min(min_heap)]
    
    return ans
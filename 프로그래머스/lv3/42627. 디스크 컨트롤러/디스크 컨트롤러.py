from heapq import heappush, heappop

def solution(jobs):
    jobs.sort()
    
    heap = []
    ans = 0
    last, time = -1, jobs[0][0]
    count, n  = 0, len(jobs)
    while count < n:  # time +1 늘리면서 텀이 짧은것을 우선으로 수행
        for r, t in jobs:
            if last < r <= time:  # last와 time은 다름 (else문에 time +=1)
                heappush(heap, (t,r))
        if len(heap) > 0:
            term, req = heappop(heap)
            count += 1
            ans += (term + time-req)
            last = time
            time += term
            
        else:
            time += 1
  
    return ans//n
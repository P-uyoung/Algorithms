def solution(citations):   
    citations.sort(reverse=True)
    ans = 0
    for i, fi in enumerate(citations):
        ans = max(min(i+1,fi), ans)
    return ans
        
    
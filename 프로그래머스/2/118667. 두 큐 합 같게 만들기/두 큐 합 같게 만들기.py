def solution(que1, que2):
    n = len(que1)
    que1 += que2
    half, remain = divmod(sum(que1), 2)
    if remain:
        return -1
    
    start, end = 0, n-1
    ans = 0
    que1_sum = sum(que1[start:end+1])
    while que1_sum != half and start < 2*n and end <3*n-1:
        if que1_sum > half:
            que1_sum -= que1[start]
            start += 1
        elif que1_sum < half:
            end += 1
            que1_sum += que1[end%(2*n)]
        ans += 1
    
    if que1_sum != half:
        return -1
    return ans
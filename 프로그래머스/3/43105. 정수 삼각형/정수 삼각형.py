from collections import deque

def solution(triangle):
    n = len(triangle)
    dp = [[0]*k for k in range(1,n+1)]
    dp[0][0] = triangle[0][0]

    for y in range(n):
        end = len(triangle[y])
        for x in range(end):
            if x == 0:
                dp[y][0] = dp[y-1][0]+triangle[y][0]
            elif x == end-1:
                dp[y][end-1] = dp[y-1][end-2] + triangle[y][end-1]
            else:
                dp[y][x] = max(dp[y-1][x-1]+triangle[y][x], dp[y-1][x]+triangle[y][x])
    # print(dp)
    return max(dp[n-1])
                      
        
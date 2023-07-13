import math
c, n = map(int, input().split())
dp = [[1e9]*(n+1) for _ in range(c+1)]
vals = [tuple(map(int, input().split())) for _ in range(n)]
for i, (cost, val) in enumerate(vals):
    for p in range(1,c+1):
        if p > val:
            dp[p][i+1] = min(dp[p-val][i+1]+cost, dp[p][i])
        else:
            dp[p][i+1] = min(cost, dp[p][i])

print(dp[-1][-1])
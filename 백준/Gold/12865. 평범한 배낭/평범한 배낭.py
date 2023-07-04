n, k = map(int, input().split())
dp  = [[0]*(n+1) for _ in range(k+1)]
buf = [tuple(map(int,input().split())) for _ in range(n)]

for i, (w,v) in enumerate(buf):
    i += 1
    for W in range(1, k+1):
        if W >= w:
            dp[W][i] = max(dp[W][i-1], dp[W-w][i-1]+v)
        else:
            dp[W][i] = dp[W][i-1]
print(dp[k][n])
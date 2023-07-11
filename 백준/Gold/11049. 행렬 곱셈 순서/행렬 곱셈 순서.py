n = int(input())
mat = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[float('inf')]*n for _ in range(n)]
for i in range(n):
    dp[i][i] = 0  
    
for l in range(1, n):
    for i in range(n-l):
        j = i+l
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + mat[i][0]*mat[k][1]*mat[j][1])
print(dp[0][-1])
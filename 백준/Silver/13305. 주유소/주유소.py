n = int(input())
city = list(map(int, input().split()))
price = list(map(int, input().split()))[:-1]
dp = [[0]*n for _ in range(n)]
for i, cost in enumerate(price):
    dp[i+1][i] = dp[i][i]
    for j in range(i,n-1):
        if i == 0:
            dp[i+1][j+1] = dp[i+1][j]+cost*city[j]

        else: 
            dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j]+cost*city[j])
print(dp[-1][-1])
n = int(input())
cost = list(map(int, input().split()))
price = list(map(int, input().split()))[:-1]
dp = [[0]*n for _ in range(n)]
for i, cash in enumerate(price):
    for j, cnt in enumerate(cost):
        if i == 0:
            dp[i+1][j+1] = dp[i+1][j] + cash*cnt
        else:
            if i > j:
                dp[i+1][j+1] = dp[i][j+1]
            else:
                dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j]+cash*cnt)
print(dp[-1][-1])
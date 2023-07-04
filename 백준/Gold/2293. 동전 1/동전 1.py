n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = [0]*(k+1) # k+1원을 나타내는 방법
dp[0] = 1

for c in coin:
    for i in range(1,k+1):
        if i-c >= 0:
            dp[i] += dp[i-c]
print(dp[k])
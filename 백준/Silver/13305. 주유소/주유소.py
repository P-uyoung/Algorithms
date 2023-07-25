n = int(input())
city = list(map(int, input().split()))
price = list(map(int, input().split()))[:-1]

dp = []
a = 0
for i in city:
    a += i
    dp.append(price[0]*a)
    

mincost = price[0]
for i, cost in enumerate(price):
    if mincost <= cost:
        continue
    mincost = cost
    for j in range(i,n-1):
        dp[j] = min(dp[j], dp[j-1]+cost*city[j])

print(dp[-1])

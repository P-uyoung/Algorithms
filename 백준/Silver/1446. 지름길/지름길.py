from copy import deepcopy
n, d = map(int, input().split())
shortcut = [tuple(map(int, input().split())) for _ in range(n)]
shortcut.sort(key = lambda x: (x[1], x[0]))
dp = list(range(d+1))

for a, b, c in shortcut:
    if b > d:
        break
    if dp[b] > dp[a]+c:
        dp = dp[:b] + [dp[a]+c+i for i in range(0,d+1-b)]
print(dp[-1])
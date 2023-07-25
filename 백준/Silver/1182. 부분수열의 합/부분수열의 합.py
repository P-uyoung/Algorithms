from itertools import combinations

n, s = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for k in range(n):
    arr = list(combinations(a, k+1))
    for i in arr:
        if sum(i) == s:
            ans += 1
print(ans)
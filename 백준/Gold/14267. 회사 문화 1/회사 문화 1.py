from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
ans = [0] * (n+1)
node = defaultdict(list)
for i, v in enumerate(list(map(int, input().split()))): 
    # if v != -1:
    node[v].append(i+1)

def dfs(i):
    if i not in node:
        return
    for j in node[i]:
        ans[j] += ans[i]
        dfs(j)
    return
    
for _ in range(m):
    i, w = map(int, input().split())
    ans[i] += w

dfs(1)

print(*ans[1:])   
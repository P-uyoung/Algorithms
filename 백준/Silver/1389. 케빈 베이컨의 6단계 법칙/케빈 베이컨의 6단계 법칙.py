from collections import defaultdict, deque

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start, end):
    q = deque()
    q.append((start, 0))
    visited = [False]*(n+1)
    visited[start] = True
    while q:
        cur, step = q.popleft()
        if cur == end:
            return step
        for nex in graph[cur]:
            if not visited[nex]:
                q.append((nex, step+1))
                visited[nex] = True

minN = 5000
ans = 0
for i in range(1, n+1):
    total = 0
    for j in range(1,n+1):
        if j == i:
            continue
        total += bfs(i, j)    
    if minN > total:
        minN = total
        ans = i
print(ans)
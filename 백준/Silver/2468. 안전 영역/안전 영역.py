from collections import deque

n = int(input())
graph = []
hight = set()
for _ in range(n):
    i = list(map(int, input().split()))
    hight.update(i)
    graph.append(i)

def bfs(x, y, h):
    q = deque()
    visited[y][x] = True
    q.append((x, y))
    while q:
        cx, cy = q.popleft()
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            nx, ny = cx+dx, cy+dy
            if 0<=nx<n and 0<=ny<n and graph[ny][nx] > h and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((nx, ny))

ans = 1
for h in hight:
    cnt = 0
    visited = [[False]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if graph[y][x] > h and not visited[y][x]:
                bfs(x, y, h)
                cnt += 1
    ans = max(ans, cnt)

print(ans)
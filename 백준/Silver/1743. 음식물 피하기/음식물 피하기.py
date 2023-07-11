from collections import deque
Y, X, k = map(int, input().split())
graph = [['.']*X for _ in range(Y)]
visited = [[False]*X for _ in range(Y)]

for _ in range(k):
    y, x = map(int, input().split())
    graph[y-1][x-1] = '#'

def combine(x, y):
    que = deque()
    que.append((x, y))
    cnt = 0
    while que:
        cx, cy = que.popleft()
        cnt += 1
        for dx, dy in (0,1), (0,-1), (1,0), (-1,0):
            nx, ny = cx+dx, cy+dy
            if 0<=nx<X and 0<=ny<Y and not visited[ny][nx]:
                if graph[ny][nx] == '#':
                    visited[ny][nx] = True
                    que.append((nx, ny))
    return cnt

ans = 0
for y in range(Y):
    for x in range(X):
        if not visited[y][x] and graph[y][x] == '#':
            visited[y][x] = True
            ans = max(ans ,combine(x, y))
print(ans)
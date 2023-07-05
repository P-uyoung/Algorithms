import sys
sys.setrecursionlimit(10**6)

n = int(input())
grid = [list(input()) for _ in range(n)]

def dfs(x, y, color):
    global visited
    if grid[y][x] not in color:
        return
    visited[y][x] = True
    for dx, dy in (1,0), (-1,0), (0,1), (0,-1):
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<n and not visited[ny][nx]:
            dfs(nx, ny, color)
    return

res = []
for tc in range(2):
    visited = [[False]*n for _ in range(n)]
    ans = 0
    for y in range(n):
        for x in range(n):
            if not visited[y][x]:
                if tc == 1 and grid[y][x] in ['R','G']:
                    dfs(x, y, ['R', 'G'])
                else:
                    dfs(x, y, [grid[y][x]])
                ans += 1
    res.append(str(ans))
print(" ".join(res))
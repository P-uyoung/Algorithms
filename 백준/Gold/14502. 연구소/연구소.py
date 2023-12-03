from itertools import combinations
from collections import deque

n, m = map(int, input().split())

def check():
    total_count = 0
    for x, y in virus:
        count = 0
        que = deque()
        que.append((x,y))
        visited[y][x] = True
        
        while que:
            cx, cy = que.popleft()
            
            for dx, dy in ((0,1), (0,-1), (1, 0), (-1,0)):
                nx, ny = cx+dx, cy+dy
                if 0<=nx<m and 0<=ny<n and not visited[ny][nx]:
                    if (nx,ny) not in combs and graph[ny][nx] == 0:
                        count += 1
                        visited[ny][nx] = True
                        que.append((nx,ny))
        total_count += count            
                        
    return one_count - 3 - total_count
    

graph = [list(map(int, input().split())) for _ in range(n)]
virus = []
one_count = 0
for y in range(n):
    for x in range(m):
        if graph[y][x] == 2:
            virus.append((x,y))
        elif graph[y][x] == 0:
            one_count += 1

# print(one_count)
ans = 0  
walls = [(i, j) for i in range(m) for j in range(n)]
for combs in combinations(walls, 3):
    flag = True
    for i, j in combs:
        if graph[j][i] != 0:
            flag= False
            break
    if flag:
        visited = [[False]*m for _ in range(n)]
        ans = max(ans, check())
        
print(ans)
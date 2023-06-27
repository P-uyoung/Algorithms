from collections import deque
n = int(input())
graph = []
for y in range(n):
    row = list(map(int, input().split()))
    if 9 in set(row):
        x = row.index(9)
        loc = (x,y)
    graph.append(row)

dx = (0,-1, 1, 0)
dy = (-1, 0, 0, 1)
def bfs(x,y,size):
    q = deque()
    q.append((x,y,size,0))
    visited = set()
    visited.add((x,y))
    shortT = n*n
    cand = ()
    while q:
        x, y, size, time = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and (nx,ny) not in visited and graph[ny][nx] <= size:
                visited.add((nx,ny))
                if 0 < graph[ny][nx] < size:
                    if shortT > time+1:
                        shortT = time+1
                        cand = (nx,ny,)
                    elif shortT == time+1:
                        if cand[1] > ny:
                            cand = (nx, ny)
                        elif cand[1] == ny and cand[0] > nx:
                            cand = (nx, ny)
                    else:
                        break
                q.append((nx,ny,size,time+1))

    if cand:
        nx, ny = cand[0], cand[1]
        graph[ny][nx] = 0
        return (nx, ny, shortT)
    else:
        return 0

size = 2
res = 0
count = 0
x,y = loc
graph[y][x] = 0
while 1:
    answer = bfs(x,y,size)
    count += 1
    if not answer:
        print(res)
        break
    nx, ny, time = answer
    res += time
    if count == size:
        size += 1
        count = 0
    x, y = nx, ny
from heapq import heappush, heappop

X, Y = map(int, input().split())
graph = [list(map(int, input())) for _ in range(Y)]

def dijk(x,y):
    dist = [[1e9]*X for _ in range(Y)]
    dist[0][0] = 0
    heap = [(0,x,y)]
    
    while heap:
        cnt, cx, cy = heappop(heap)
        if dist[cy][cx] < cnt:
            continue
        for dx, dy in (0,1), (0,-1), (1,0), (-1,0):
            nx, ny = cx+dx, cy+dy
            if nx<0 or nx>=X or ny<0 or ny>=Y:
                continue
            ncnt = cnt + graph[ny][nx]
            if dist[ny][nx] > ncnt:
                dist[ny][nx] = ncnt
                heappush(heap, (ncnt, nx, ny))
    return dist[Y-1][X-1]
print(dijk(0,0))  
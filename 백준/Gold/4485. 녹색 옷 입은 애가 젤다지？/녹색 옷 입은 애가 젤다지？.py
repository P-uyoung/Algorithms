from heapq import heappop, heappush

def dijk():
    loss = [[1e9]*n for _ in range(n)]
    loss[0][0] = graph[0][0]

    que = [(graph[0][0], 0, 0)]
    while que:
        cur_loss, x, y = heappop(que)

        # 우선순위큐로써, 이미 방문했던 노드라면 그것이 최솟값
        if loss[y][x] < cur_loss:
            continue
        
        for dx, dy in (0,1), (0,-1), (1,0), (-1,0):
            nx, ny = x+dx, y+dy
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            next_loss = cur_loss + graph[ny][nx]
            # 현재 노드를 통과하여 인접 노드까지의 거리가 더 짧은 경우
            if loss[ny][nx] > next_loss:
                loss[ny][nx] = next_loss
                heappush(que, (next_loss, nx, ny))
    return loss[n-1][n-1]
i = 1
while 1:
    n = int(input())
    if n == 0:
        break
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    print("Problem %d: %d" %(i,dijk()))
    i += 1


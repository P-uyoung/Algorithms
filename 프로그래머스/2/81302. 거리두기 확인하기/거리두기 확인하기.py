from collections import deque
def solution(places):
    def bfs(i, j):
        que = deque()
        que.append((i,j, 0, False))
        visited = [[False]*5 for _ in range(5)]
        visited[i][j] = True

        while que:
            i, j, dist, pati = que.popleft()
            
            if dist >= 2:
                continue
                
            for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
                ni, nj = i+di, j+dj
                if 0<= ni < 5 and 0<= nj < 5 and not visited[ni][nj]:
                    if place[ni][nj] == 'P':
                        if not pati:
                            return 1
                    else:
                        visited[ni][nj] = True
                        if place[ni][nj] == 'X':
                            que.append((ni, nj, dist+1, True)) 
                        else:
                            que.append((ni, nj, dist+1, False))
                        
        return 0

    ans = []
    for place in places:
        all = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if bfs(i,j):
                        all = False
                        break
            if not all:
                break
        if all: ans.append(1)
        else: ans.append(0)
        
    return ans

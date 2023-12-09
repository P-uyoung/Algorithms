def solution(board):
    answer = 400000
    N = len(board)
    dp = [[[400000 for i in range(N)] for i in range(N)] for i in range(4)]
    directions = [(0, 1, 0), (1, 0, 1), (0, -1, 2), (-1, 0,3)]
    q = []
    q.append((0,0,1,0)) # (x,y,dir,cost)
    q.append((0,0,0,0))
    
    while q:
        x,y,d,c= q.pop(0)
        for i in directions:
            nx = x + i[0]
            ny = y + i[1]
            if 0<=nx<=N-1 and 0<=ny<=N-1 and board[ny][nx] == 0:
                add = 100 if d==i[2] else 600
                if dp[i[2]][ny][nx] > c+add:
                    dp[i[2]][ny][nx] = c+add
                    # if nx == N-1 and ny==N-1:
                    #     continue
                    q.append((nx,ny, i[2], dp[i[2]][ny][nx]))
    for i in range(4):
        answer = min(answer,dp[i][N-1][N-1])
    return answer
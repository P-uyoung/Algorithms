# https://school.programmers.co.kr/learn/courses/30/lessons/1844

def solution(maps):
    x_move = [1, 0, -1, 0]
    y_move = [0, 1, 0, -1]
    x_h, y_h = len(maps[0]), len(maps)
    que = [[0,0,1]]    
    
    while que:
        x, y, d = que.pop(0)
        for i in range(4):
            nx = x + x_move[i]
            ny = y + y_move[i]
            
            if (0<=nx<x_h) and (0<=ny<y_h):
                if maps[ny][nx] == 1 or maps[ny][nx] > d+1:
                    maps[ny][nx] = d+1
                    if nx == x_h-1 and ny == y_h-1:
                        return d+1
                    
                    que.append((nx,ny,d+1))
                    
    return -1
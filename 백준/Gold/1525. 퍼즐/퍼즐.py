from collections import deque

# 3x3 퍼즐의 목표 상태
goal = '123456780'

# 주어진 위치에서 이동할 수 있는 4가지 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start):
    visited = set()
    queue = deque([(start, 0)])
    visited.add(start)
    
    while queue:
        curr, count = queue.popleft()
        
        if curr == goal:
            return count
        
        z = curr.index('0')
        x, y = z // 3, z % 3
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < 3 and 0 <= ny < 3:
                nz = nx * 3 + ny
                next_state = list(curr)
                next_state[z], next_state[nz] = next_state[nz], next_state[z]
                next_state = ''.join(next_state)
                
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, count + 1))
                    
    return -1

# 입력 받기
puzzle = [list(map(int, input().split())) for _ in range(3)]
start = ''
for i in range(3):
    for j in range(3):
        start += str(puzzle[i][j])

print(bfs(start))

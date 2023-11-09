import copy

def solution(m, n, board):
    # 문자열로 주어진 게임 보드를 2차원 리스트로 변환합니다.
    board = [list(s) for s in board]
    # 점수를 계산할 변수를 초기화합니다.
    totalScore, score = 0, 0
    
    # 게임이 진행되는 동안 반복합니다.
    while True:
        # 현재까지의 총 점수에 이번 라운드의 점수를 더합니다.
        totalScore += score
        # 이번 라운드의 점수를 초기화합니다.
        score = 0
        # 보드의 상태를 깊은 복사하여 블록을 제거할 보드2를 생성합니다.
        board2 = copy.deepcopy(board)
        
        # 보드를 스캔하여 제거할 블록을 찾습니다.
        for r in range(m-1):
            for c in range(n-1):
                # 인접한 블록을 검사합니다.
                d = [(r+1, c), (r, c+1), (r+1, c+1)]
                # 현재 블록을 포함한 2x2 블록의 좌표를 저장합니다.
                idx = [(r,c)]
                # 2x2 블록이 같은 문자로 이루어져 있는지 확인합니다.
                for dr, dc in d:
                    if board[r][c] == board[dr][dc]:
                        idx.append((dr,dc))
                # 같은 문자로 이루어진 2x2 블록을 찾으면 제거합니다.
                if len(idx) == 4:
                    for y, x in idx:
                        # 해당 블록을 제거하고 점수를 증가시킵니다.
                        if board2[y][x] != 0:
                            board2[y][x] = 0
                            score += 1
                            
        # 제거할 블록이 있었다면, 블록을 떨어뜨립니다.
        if score:
            cols = []
            # 각 열에 대해 제거된 블록의 위에 있는 블록들을 아래로 떨어뜨립니다.
            for c in range(n):
                col = [board2[r][c] for r in range(m) if board2[r][c] != 0]
                # 빈 자리를 0으로 채웁니다.
                col = [0]*(m-len(col)) + col 
                cols.append(col)
            
            # 각 열을 다시 보드에 배치합니다.
            for c in range(n):
                for r in range(m):
                    board[r][c] = cols[c][r]
        else:
            # 더 이상 제거할 블록이 없으면 게임을 종료합니다.
            break
            
    # 총 점수를 반환합니다.
    return totalScore

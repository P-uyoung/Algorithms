def solution(board, moves):
    n = len(board)
    columns = [[]for i in range(n)]
    stack = []
    answer = 0
    
    # 각 열 초기화
    for i in range(n):
        end = n-1
        
        while True:
            item = board[end][i]
            
            if item != 0:
                columns[i].append(item)
                if end != 0:
                    end -= 1
                else: break
                
            else:
                break

    
    # 쌓아두고
    for mv in moves:
        if len(columns[mv-1]) != 0:
            item = columns[mv-1].pop()
            if len(stack) == 0 :
                stack.append(item)
                
            else:
                if item == stack[-1]:
                    stack.pop()
                    answer += 2
                
                else:
                    stack.append(item)

                
                
                      
    return answer

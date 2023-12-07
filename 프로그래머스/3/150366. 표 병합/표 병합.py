def solution(commands):
    l = 51
    table = [['EMPTY']*l for _ in range(l)]
    merged = []
    ans = []

    for cmd in commands:
        cmd = cmd.split()
        # print(cmd[0])
        # print(table)
        if cmd[0] == 'UPDATE' and len(cmd) == 4:
            r, c = int(cmd[1]), int(cmd[2])
            value = cmd[3]
            idx = -1
            for i, m in enumerate(merged):
                if (r, c) in m:
                    idx = i
                    break
            if idx != -1:
                for rr, cc in merged[idx]:
                    table[rr][cc] = value
            else:
                table[r][c] = value
    
        elif cmd[0] == 'UPDATE':
            value, new_value = cmd[1], cmd[2]
            for i in range(1, l):
                for j in range(1, l):
                    if table[i][j] == value:
                        table[i][j] = new_value
                        
        elif cmd[0] == 'MERGE':
            r1, c1, r2, c2 = map(int, cmd[1:5])
            if (r1, c1) == (r2, c2):
                continue
            
            value = None
            follow_first= False
            if table[r1][c1] != 'EMPTY':
                value = table[r1][c1]
                table[r2][c2] = value
                follow_first= True
            elif table[r2][c2] != 'EMPTY':
                value = table[r2][c2]
                table[r1][c1] = value

            exist_first, exist_second = -1, -1
            for i, m in enumerate(merged):
                if (r1, c1) in m:
                    exist_first = i
                if (r2, c2) in m:
                    exist_second = i
                if exist_first != -1 and exist_second != -1:
                    break
            
            if exist_first == -1 and exist_second == -1:
                merged.append(set([(r1, c1), (r2, c2)]))
                
            elif exist_first == exist_second:
                continue
            elif exist_first != -1 and exist_second == -1:
                if value is not None and not follow_first:
                    for rr, cc in merged[exist_first]:
                        table[rr][cc] = value
                merged[exist_first].add((r2, c2))
            elif exist_first == -1 and exist_second != -1:
                if value is not None and follow_first:
                    for rr, cc in merged[exist_second]:
                        table[rr][cc] = value
                merged[exist_second].add((r1, c1))
            else: 
                if value is not None and follow_first:
                    for rr, cc in merged[exist_second]:
                        table[rr][cc] = value
                elif value is not None and not follow_first:
                    for rr, cc in merged[exist_first]:
                        table[rr][cc] = value
                merged[exist_first].update(merged[exist_second])
                merged.pop(exist_second)
                
        elif cmd[0] == 'UNMERGE':
            r, c = int(cmd[1]), int(cmd[2])
            unmerge_idx = None
            for i, m in enumerate(merged):
                if (r, c) in m:
                    unmerge_idx = i
                    break

            if unmerge_idx is not None:
                for rr, cc in merged[unmerge_idx]:
                    if (rr, cc) != (r, c):
                        table[rr][cc] = "EMPTY"
                merged.pop(unmerge_idx)
                
        elif cmd[0] == 'PRINT':
            r, c = int(cmd[1]), int(cmd[2])
            ans.append(table[r][c])

    return ans
  
# print(solution(["UPDATE 1 1 menu", "MERGE 1 1 1 2", "MERGE 1 1 1 3", "MERGE 1 1 1 4", "MERGE 1 2 1 3", "UPDATE 1 1 hansik", "PRINT 1 1", "PRINT 1 2", "PRINT 1 3", "PRINT 1 4"]))
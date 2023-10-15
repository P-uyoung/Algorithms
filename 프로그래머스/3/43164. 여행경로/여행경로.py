from collections import defaultdict

def solution(tickets):
    path = defaultdict(list)
    exist = defaultdict(int)   # visited = set() 대신,
    for a, b in tickets:
        path[a].append(b)
        # path[b].append(a)
        exist[(a,b)] += 1
        
    path = {k: sorted(v) for k, v in path.items()}
        
    n = len(tickets)
    # visited = set()  # 동일한 티켓을 고려 못함
    def dfs(start, ans):
        if sum(exist.values()) == 0:
            return ans
        
        if start not in path:
            return
        
        for end in path[start]:
            if exist[(start,end)]:
                exist[(start,end)] -= 1
                ans.append(end)
                
                result = dfs(end, ans)
                if result:
                    return result
                
                exist[(start,end)] += 1
                ans.pop()

    return dfs('ICN', ['ICN'])

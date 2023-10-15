from collections import defaultdict

def solution(tickets):
    path = defaultdict(list)
    visited = defaultdict(int)
    for a, b in tickets:
        path[a].append(b)
        # path[b].append(a)
        visited[(a,b)] += 0
        
    path = {k: sorted(v) for k, v in path.items()}
        
    n = len(tickets)
    # visited = set()  # 동일한 티켓을 고려 못함
    def dfs(start, ans):
        if len(visited) == n:
            return ans
        
        if start not in path:
            return
        
        for end in path[start]:
            if not visited[(start,end)]:
                visited[(start,end)] -= 1
                ans.append(end)
                
                result = dfs(end, ans)
                if result:
                    return result
                
                visited[(start,end)] += 1
                ans.pop()

    return dfs('ICN', ['ICN'])
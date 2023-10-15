from collections import deque

def solution(n, vertex):
    graph = [[] for _ in range(n+1)]
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)
        
    lev = -1
    que = deque()
    que.append((1, 0))
    visited = [False] *(n+1)
    visited[1] = True
    
    while que:
        cur_node, cur_lev = que.popleft()
        if cur_lev > lev: 
            lev = cur_lev
            ans = 1
        else:
            ans += 1
            
        for nxt_node in graph[cur_node]:
            if not visited[nxt_node]:
                que.append((nxt_node, lev+1))
                visited[nxt_node] = True
    return ans
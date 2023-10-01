# DFS
# https://school.programmers.co.kr/learn/courses/30/lessons/49189

graph = []
dp = []
visited = []

def bfs():
    q = []
    q.append(1)
    
    while q:
        cur = q.pop(0)
        # visited[cur] = True
        
        for nxt in graph[cur]:
            # if visited[nxt] == False:
                if dp[nxt] == 0:
                    if dp[nxt] == 0 or dp[nxt] > dp[cur]+1:
                        dp[nxt] = dp[cur]+1 
                        q.append(nxt)  
                    else:
                        pass
            
def solution(n, vertex):
    for i in range(n+1):
        graph.append([])
        dp.append(0)
        visited.append(False)
        
    for u, v in vertex:
        graph[u].append(v)
        graph[v].append(u)

    # print(graph)
    bfs()
    # print(dp)
    count = max(dp)
    answer = dp.count(count)

    return answer

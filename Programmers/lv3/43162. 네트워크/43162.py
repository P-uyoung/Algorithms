# DFS
# https://school.programmers.co.kr/learn/courses/30/lessons/43162

def dfs(k, graph, visited):
    visited[k] = True
    [dfs(i, graph, visited) for i in graph[k] if visited[i]==False]
    return 

        
def solution(n, computers):
    answer = 0
    graph = [[] for i in range(n)]

    for i, arr in enumerate(computers):
        for j in range(n):
            if i != j and arr[j]==1:
                graph[i].append(j)
    print
    visited = [False for i in range(n)]
    for i in range(n):
        if visited[i] == False:
            answer += 1
            print(i)
            dfs(i, graph, visited)
                
    print(answer)      
    return answer

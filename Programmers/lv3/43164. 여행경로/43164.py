# DFS
# https://school.programmers.co.kr/learn/courses/30/lessons/43164

answer = []
def dfs(start, tickets, visited, result):
    global answer

    if visited.count(True)==len(tickets):
        if answer == []:
            answer = result
            return

        else:
            for a,b in zip(answer, result):
                if a > b:
                    answer = result
                    break
                elif a < b:
                    break
            return 
    
    for i, ticket in enumerate(tickets):
        if ticket[0] == start and visited[i]==False:
            visited[i] = True
            dfs(ticket[1], tickets, visited, result+[ticket[1]])
            visited[i] = False


def solution(tickets):
    visited = [False for i in range(len(tickets))]
    dfs('ICN', tickets, visited, ['ICN'])

    return answer

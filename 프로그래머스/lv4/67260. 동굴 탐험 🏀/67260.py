# 위상정렬 (사이클이 있는지 판단)
# https://school.programmers.co.kr/learn/courses/30/lessons/67260

from collections import deque

def bfs(room, n):
    indegree = [0 for _ in range(n)]
    q = deque()
    q.append(0)
    
    while q:
        current = q.popleft()
        for i in room[current]:
            room[i].remove(current)
            indegree[i] += 1
            q.append(i)
    return room, indegree
    
def solution(n, path, order):
    answer = True
    room_tmp = [[] for _ in range(n)]
    
    for a, b in path:
        room_tmp[a].append(b)
        room_tmp[b].append(a)
        
    room, indegree = bfs(room_tmp, n)
    for a, b in order:
        room[a].append(b)
        indegree[b] += 1

    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)
    
    # 노드개수만큼 돌기 전에 queue가 비면 False, 그 외엔 True
    for i in range(n):
        if not q:
            answer = False
            break
        current = q.popleft()
        for j in room[current]:
            indegree[j] -= 1
            if indegree[j] == 0:
                q.append(j)
    
    return answer
# BFS
# https://school.programmers.co.kr/learn/courses/30/lessons/43163

def get_next(cur, words):
    for nxt in words:
        count = 0
        for c, n in zip(cur, nxt):
            if c != n:
                count += 1
            if count > 1:
                break
        if count == 1:
            yield nxt

def solution(begin, target, words):
    dist = {'begin':0}
    q = []
    q.append(begin)

    while q:
        cur = q.pop(0)

        for nxt in get_next(cur, words):
            if nxt not in dist:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)
    return dist.get(target, 0)



#### DFS (내풀이)

minima = 51
def check(a, b):
    N = len(a)
    count = 0
    for i in range(N):
        if a[i] != b[i]:
            count +=1
        if count > 1:
            return False
    if count == 1: # begin이 words에 존재할 수 있음
        return True

def bfs(w, target, words, visited):
    global minima
    cnt = visited.count(True)
    if cnt > minima:
        return
    if w == target and minima > cnt:
        minima = cnt
        return minima

    for i, nxt in enumerate(words):
        if visited[i] == False and check(w,nxt):
            visited[i]=True
            bfs(nxt, target, words, visited)
            visited[i]=False

    return minima

def solution(begin, target, words):
    visited = [False for i in range(len(words))]
    answer = 51

    for i, w in enumerate(words):
        if check(begin, w):
            visited[i] = True
            answer = min(answer, bfs(w, target, words, visited))
            visited[i] = False
    if answer == 51:
        return 0
    return answer

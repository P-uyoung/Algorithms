# Topology Sort (위상 정렬)
# https://school.programmers.co.kr/learn/courses/30/lessons/76503
# 문제풀이 사이트, https://kante-dev.tistory.com/entry/Programmers-%EB%AA%A8%EB%91%90-0%EC%9C%BC%EB%A1%9C-%EB%A7%8C%EB%93%A4%EA%B8%B0

from collections import deque

def solution(a, edges):
    ed = [set() for _ in range(len(a))]
    visit = [False]*len(a)
    if sum(a) != 0:
        return -1
    for i in edges:
        ed[i[0]].add(i[1])
        ed[i[1]].add(i[0])
    q = deque()
    cnt = 0

    for i in range(len(ed)):
        if len(ed[i]) == 1:
            q.append(i)
    while q:
        front = q.popleft()
        if len(ed[front]) == 0:
            continue
        temp = ed[front].pop()
        if a[front] != 0:
            cnt += abs(a[front])
            a[temp] += a[front]
            a[front] = 0
        ed[temp].remove(front)
        if len(ed[temp]) == 1:
            q.append(temp)
    return cnt
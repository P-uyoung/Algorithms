[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/86971) 

### 구분
완전탐색 

### 문제 설명  
(트리)전력망 최대한 비슷한 개수로 둘로 나누기

<br/>

> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges





## 3. 전력망 나누기 (프로그래머스_level2)

(1) 그래프 안만들고, set

\- set 두 번 돌기

\```python

def solution(n, wires):

​    ans = n

​    for sub in (wires[i+1:] + wires[:i] for i in range(n)):     ## Good

​        s = set(sub[0])

​        [s.update(v) for _ in sub for v in sub if set(v) & s]

​        ans = min(ans, abs(n-2*len(s)))

\```

<br/>

(2) DFS로 풀기

\- 자료구조 : 그래프

\```python

def dfs(v, graph, visited):

​    visited[v] = True

​    return sum([1] + [DFS(u, graph, visited) for u in graph[v] if not visited[u]])   ## Good

def solution(n, wires):

​    answer = 1000

​    graph = [[] for _ in range(n+1)]

​    for u, v in wires:

​        graph[u].append(v)

​        graph[v].append(u)

​    for u, v in wires:

​        visited = [False for _ in range(n+1)]

​        visited[v] = True

​        answer = min(answer, abs((n-2*dfs(u, graph, visited))))

​        

​    return answer

\```

(3) BFS로 풀기

\- 자료구조 : 그래프

\```python

graph = []

numChild = []

def countChild(v):

​    if numChild[v] != -1:

​        return numChild[v]

​    count = len(graph[v])

​    for child in graph[v]:

​        count += countChild(child)

​    numChild[v] = count

​    return count

def bfs(n):

​    q = []

​    visited = [False for _ in range(n+1)]

​    q.append(1)

​    visited[1] = True

​    while q:

​        cur = q.pop(0)

​        for nex in graph[cur]:

​            q.append(nex)

​            visited[nex] = True

​            graph[nex].remove(cur)

def solution(n, wires):

​    for i in range(n+1):

​        graph.append([])

​        numChild.append(-1)

​    for u, v in wires:

​        graph[u].append(v)

​        graph[v].append(u)

​    bfs(n)

​    countChild(1)

​    return min(map(lambda v: abs((n-(v+1))-(v+1)), numChild))         # + 1은 parent node와의 연결

\```
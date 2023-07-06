from collections import deque
from collections import defaultdict

n, m = map(int,input().split())
tree = defaultdict(list)
for _ in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))
    
def bfs(start, end):
    que = deque()
    que.append(start)
    dist = [-1] * (n+1)
    dist[start] = 0
    while que:
        node = que.popleft()
        if  node == end:
            return dist[node]
        for next_node, distance in tree[node]:
            if dist[next_node] == -1:
                que.append(next_node)
                dist[next_node] = dist[node] + distance

for _ in range(m):
    start, end = map(int, input().split())
    print(bfs(start, end))
import sys

n, m = map(int, input().split())

graph = {node: [] for node in range(1, n+1)}
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a].append((c,b))

distances = {node: float('inf') for node in graph}
distances[1] = 0

for _ in range(n-1):
    for node in range(1, n+1):
        for edge, adjacent in graph[node]:
            if distances[node] + edge < distances[adjacent]:
                distances[adjacent] = distances[node] + edge

for node in range(1, n+1):
    for edge, adjacent in graph[node]:
        # 더 줄일 수 가 있다면, 음수 가중치
        if distances[node] + edge < distances[adjacent]:
            print(-1)
            exit(0)
            
del distances[1]
ans = [dist if dist != float('inf') else -1 for _, dist in distances.items()]
print(*ans)
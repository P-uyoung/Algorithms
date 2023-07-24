n, m = map(int, input().split())
graph = [[int(j) for j in input()] for _ in range(n)]

def checkEdge(k):
    while k > 1:
        for x in range(m-k+1):
            for y in range(n-k+1):
                a = graph[y][x]
                if a == graph[y][x+k-1] and a == graph[y+k-1][x] and a == graph[y+k-1][x+k-1]:
                    return k*k
        k -= 1
    return k*k
print(checkEdge(min(n, m)))
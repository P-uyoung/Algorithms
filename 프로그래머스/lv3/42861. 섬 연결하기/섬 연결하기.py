def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]
    
    for cost in costs:
        a, b, c = cost
        if find(parent, a) != find(parent, b): # 사이클 생기는지 확인
            answer += c
            union(parent, a, b)
            
    return answer

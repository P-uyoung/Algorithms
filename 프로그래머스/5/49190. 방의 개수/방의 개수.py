from collections import defaultdict
def solution(arrows):
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    cx, cy = 0, 0
    graph = defaultdict(set)
    visited = set()
    visited.add((cx,cy))
    ans = 0
    for a in arrows:
        for _ in range(2):
            nx, ny = cx+dx[a], cy+dy[a]
            if (nx,ny) in visited and (nx,ny) not in graph[(cx,cy)]:
                ans += 1
            visited.add((nx,ny))
            graph[(cx,cy)].add((nx,ny))
            graph[(nx,ny)].add((cx,cy))
            cx, cy = nx, ny
    #         print(visited)
    # print(graph)   
    return ans
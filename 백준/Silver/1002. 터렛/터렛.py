import math
tc = int(input())
for _ in range(tc):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if (x1, y1) == (x2, y2):
        if r1 == r2:
            print(-1)
        else:
            print(0)
        continue
    
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if d == r1+r2:
        print(1)
    elif d > r1+r2:
        print(0)
    elif d + r1 == r2 or d + r2 == r1:
        print(1)
    elif d + r1 > r2 and d + r2 > r1 and d <r1+r2:
        print(2)
    
    else:
        print(0)
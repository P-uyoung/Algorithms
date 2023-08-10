import sys
n = int(sys.stdin.readline())
ans = [11] * n
for i, v in enumerate(list(map(int, sys.stdin.readline().split()))):
    count  = len([num for num in ans[:v] if num > i+1])
    next = v - count
    x = v
    while next or ans[x] < i+1:
        if ans[x] > i+1:
            next -= 1
        x += 1
        

    ans[x] = i + 1

print(*ans)
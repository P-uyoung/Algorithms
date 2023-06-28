import sys
input = sys.stdin.readline
output = sys.stdout.write
def init(node, start, end):
    if start == end:
        tree[node] = l[start]
    else:
        mid = (start+end)//2
        tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
    return tree[node]
def subSum(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end) // 2
    return subSum(node*2, start, mid, left, right) + subSum(node*2+1, mid+1, end, left, right)
def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    if start != end:
        mid = (start+end)//2
        update(node*2, start, mid, index, diff)
        update(node*2+1, mid+1, end, index, diff)
n, q = map(int, input().strip().split())
l = list(map(int, input().strip().split()))
tree = [0]*(n*4)
init(1, 0, n-1)
for _ in range(q):
    x, y, a, b = map(int, input().strip().split())
    if x > y:
        x, y = y, x
    output("%d\n" %subSum(1, 0, n-1, x-1, y-1))
    diff = b - l[a-1]
    l[a-1] = b
    update(1, 0, n-1, a-1, diff)

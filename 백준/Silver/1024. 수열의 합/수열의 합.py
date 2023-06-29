N, L = map(int, input().split())
res = []
while not res and L <= 100:
    n = (2*N+L**2-L) / (2*L)
   
    if n >= L-1 and int(n) == n:
        res = [v+1 for v in range(int(n)-L, int(n))]
    L += 1
if not res:
    print(-1)
else:
    print(' '.join(str(v) for v in res))
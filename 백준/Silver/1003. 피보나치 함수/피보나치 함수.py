memo = {0:(1,0), 1:(0,1)}
def fibo(n):
    if n not in memo:
        memo[n] = [a+b for a, b in zip(fibo(n-1),fibo(n-2))]
    return memo[n]

for _ in range(int(input())):    
    ans = fibo(int(input()))
    print(f'{ans[0]} {ans[1]}')
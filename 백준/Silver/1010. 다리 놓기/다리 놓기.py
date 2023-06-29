memo = {}

def factorial(n):
    if n== 0 or n == 1:
        return 1
    if n not in memo:
        memo[n] = n * factorial(n-1)
    return memo[n]

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(factorial(m) // (factorial(m-n) * factorial(n)))
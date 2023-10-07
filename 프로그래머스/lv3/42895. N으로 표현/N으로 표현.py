def solution(N, number):
    if N == number:
        return 1
    
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(N)*i))
    
    for i in range(2,9):
        for j in range(i-1, i//2-1, -1):
            for a in dp[j]:
                for b in dp[i-j]:
                    dp[i].add(a+b)
                    dp[i].add(a-b)
                    dp[i].add(a*b)
                    if a != 0:
                        dp[i].add(int(b/a))
                    if b != 0:
                        dp[i].add(int(a/b))

        if number in dp[i]:
            return i
    
    return -1
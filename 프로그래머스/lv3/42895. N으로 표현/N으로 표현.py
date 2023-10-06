def solution(N, number):
    if N == number:
        return 1

    # dp[i]는 N을 i번 사용하여 만들 수 있는 숫자들의 집합
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))

    for i in range(1, 9):
        for j in range(1, i):
            for num1 in dp[j]:
                for num2 in dp[i-j]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)

        if number in dp[i]:
            return i

    return -1
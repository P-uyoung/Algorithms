def solution(alp, cop, problems):
    # 최대 알고력과 코딩력 계산
    max_alp = max(max(p[0] for p in problems), alp)
    max_cop = max(max(p[1] for p in problems), cop)

    # 다차원 배열 초기화
    dp = [[float('inf')] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0

    for cur_alp in range(alp, max_alp + 1):
        for cur_cop in range(cop, max_cop + 1):
            # 현재 상태에서 1시간 공부로 알고력 또는 코딩력 향상
            if cur_alp < max_alp:
                dp[cur_alp + 1][cur_cop] = min(dp[cur_alp + 1][cur_cop], dp[cur_alp][cur_cop] + 1)
            if cur_cop < max_cop:
                dp[cur_alp][cur_cop + 1] = min(dp[cur_alp][cur_cop + 1], dp[cur_alp][cur_cop] + 1)
            
            # 문제를 풀어서 알고력과 코딩력 향상
            for a_req, c_req, a_rwd, c_rwd, cost in problems:
                if cur_alp >= a_req and cur_cop >= c_req:
                    next_alp = min(max_alp, cur_alp + a_rwd)
                    next_cop = min(max_cop, cur_cop + c_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[cur_alp][cur_cop] + cost)

    return dp[max_alp][max_cop]
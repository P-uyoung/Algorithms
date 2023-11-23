def solution(alp, cop, problems):
    max_alp = max(max(p[0] for p in problems), alp)
    max_cop = max(max(p[1] for p in problems), cop)
        
    dp = [[float('inf')]* (max_cop+1) for _ in range(max_alp+1)]
    dp[alp][cop] = 0
    for cur_alp in range(alp, max_alp+1):
        for cur_cop in range(cop, max_cop+1):
            if cur_alp < max_alp:
                dp[cur_alp+1][cur_cop] = min(dp[cur_alp+1][cur_cop], dp[cur_alp][cur_cop]+1)
            if cur_cop < max_cop:
                dp[cur_alp][cur_cop+1] = min(dp[cur_alp][cur_cop+1], dp[cur_alp][cur_cop]+1)
        
            for req_alp, req_cop, rwd_alp, rwd_cop, cost in problems:
                if cur_alp >= req_alp and cur_cop >= req_cop:
                    next_alp = min(max_alp, cur_alp+rwd_alp)
                    next_cop = min(max_cop, cur_cop+rwd_cop)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[cur_alp][cur_cop]+cost)
    return dp[max_alp][max_cop]
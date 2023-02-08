from itertools import permutations
def solution(k, dungeons):
    answer = 0
    for order in permutations(range(len(dungeons))):
        cur = k

        local_ans = 0

        for i in order:
            require, consum = dungeons[i]
            if require <= cur:
                cur -= consume
                loca_answer += 1
        answer = max(answer, local_ans)     # cleancode
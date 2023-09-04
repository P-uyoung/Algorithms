from collections import defaultdict

def solution(gems):
    total_gems = len(set(gems))
    gem_dict = defaultdict(int)
    
    start, end = 0, 0
    answer = [0, float('inf')]
    
    while end < len(gems):
        # end 포인터를 이동하면서 보석 개수를 증가
        gem_dict[gems[end]] += 1
        end += 1
        
        # 모든 종류의 보석을 포함하면 start 포인터를 이동
        while len(gem_dict) == total_gems:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            
            gem_dict[gems[start]] -= 1
            if gem_dict[gems[start]] == 0:
                del gem_dict[gems[start]]
            start += 1
            
    return [answer[0] + 1, answer[1]]
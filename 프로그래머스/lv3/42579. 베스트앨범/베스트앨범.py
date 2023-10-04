from collections import defaultdict

def solution(genres, plays):
    musics = defaultdict(list)
    chart = defaultdict(int)
    for i, (k, v) in enumerate(zip(genres, plays)):
        musics[k].append((v, i))
        chart[k] += v
    
    answer = []
    chart = dict(sorted(chart.items(), key=lambda x:x[1], reverse=True))
    for k, _ in chart.items():
        values = sorted(musics[k], key=lambda x:(x[0], -x[1]), reverse=True)
        answer.append(values[0][1])
        if len(values) >= 2:
            answer.append(values[1][1])

    return answer
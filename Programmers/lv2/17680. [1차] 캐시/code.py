from collections import deque
def solution(cacheSize, cities):
    answer = 0
    q = deque()
    
    if cacheSize == 0:
        return 5*len(cities)
    
    for city in cities:
        city = city.casefold()
        if city in q:
            answer += 1
            q.remove(city)
            q.append(city)
        else:
            answer += 5
            q.append(city)
            if len(q) > cacheSize:
                q.popleft()
    return answer
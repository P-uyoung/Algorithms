import re
def solution(s):
    dic = {}
    n = 1
    result = []
    
    s = s.split('},')
    for ss in s:
        ss = re.findall(r'\d+',ss)
        dic[len(ss)] = set(ss)
        n = max(n,len(ss))
        if len(ss) == 1:
            result.append(int(ss.pop()))
      
    for i in range(2,n+1):
        intersection = dic[i] - dic[i-1]
        result.append(int(intersection.pop()))
    return result  
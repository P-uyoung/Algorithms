from collections import Counter
import math
import re

def solution(str1, str2):
    answer = 0
    n = len(str1)
    m = len(str2)
    input1 = []
    input2 = []
    
    input1 = [str1[i:i+2].casefold() for i in range(n-1) if str1[i:i+2].isalpha()]  #if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    dic1 = dict(Counter(input1))
    
    input2 = [str2[i:i+2].casefold() for i in range(m-1) if str2[i:i+2].isalpha()]
    dic2 = dict(Counter(input2))

    # 예외처리
    if not input1 and not input2:
        return 65536
    
    keys_set = set(list(dic1.keys()) + list(dic2.keys()))
    intersectN = 0
    for key in keys_set:
        if key in dic1 and key in dic2:
            intersectN += min(dic1[key], dic2[key])
    unionN = len(input1) + len(input2) - intersectN
    
    answer = intersectN / unionN
    return math.trunc(answer*65536)
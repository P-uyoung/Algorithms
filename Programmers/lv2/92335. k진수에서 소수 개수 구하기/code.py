import math
import re 

def solution(n, k):
    answer = 0
    
    convert = ''
    while n > 0:
        n, r = divmod(n,k)
        convert += str(r)
    convert = convert[::-1]    
    convert = re.findall('[^0]+', convert)
    
    def isPrime(a):
        end = int(math.sqrt(a))
        for i in range(2,end+1):
            if a % i == 0:
                return False        
        return True
    
    for v in convert:
        v = int(v)
        if v != 1 and isPrime(v):
            answer += 1
    
    return answer
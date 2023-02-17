# DFS
# https://school.programmers.co.kr/learn/courses/30/lessons/60058

def check(u):
    if u[0] == ')':
        return False
    left = 0
    for i in range(len(u)):
        if u[i]== '(':
            left += 1
        else:
            left -= 1
        if left < 0:
            return False
    return True

def remove_reverse(u):
    reverse = ""
    for i in range(1,len(u)-1):
        if u[i] == "(":
            reverse += ")"
        else:
            reverse += "("
            
    return reverse

def dfs(p):
    N = len(p)
    
    if N == 0:
        return ""
    
    right, left = 0,0
    for i in range(N):
        if p[i] == "(":
            left += 1
        else:
            right += 1
        
        if (right!=0 and left!=0) and right==left:
            break
    
    u = p[:right+left]
    v = p[right+left:]
    
    if check(u):
        u += dfs(v)
        return u
    
    else:
        return "("+dfs(v)+")"+remove_reverse(u)

    
def solution(p):
    answer = ''
    N = len(p)
    
    answer = dfs(p)
    
    return answer

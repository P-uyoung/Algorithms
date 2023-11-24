from collections import deque

def shiftRow(left,center,right) : 
    left.rotate(1)
    right.rotate(1)
    center.rotate(1)
    return

def rotate(left,center,right) : 
    # left -> top
    center[0].appendleft(left.popleft())

    # top -> right
    right.appendleft(center[0].pop())

    # right -> bottom
    center[-1].append(right.pop())

    # bottom -> left
    left.append(center[-1].popleft())

def solution(rc, operations):
    '''
    left  center right
      d   deque1   d 
      e   deque2   e
      q   deque3   q
      u   deque4   u
      e   deque5   e

    left, right : deque
    center : deque[deque]
    '''

    r, c = len(rc),len(rc[0])

    # set left(x=0) and right(x=c) deque
    left,right = deque(),deque()
    for i in range(r) : 
        left.append(rc[i][0])
        right.append(rc[i][c-1])

    # set center deque (list of deque(1~c-1))
    center = deque([deque(x[1:-1]) for x in rc])

    for op in operations : 
        if op=="ShiftRow" : 
            shiftRow(left,center,right)
        else : 
            rotate(left,center,right)

    # assemble left, center and right
    res = [list(x) for x in center]
    return [[left[i]]+res[i]+[right[i]] for i in range(len(res))]
def solution(brown, yellow):
    for i in range(1, int(yellow**0.5)+1):
        if yellow % i == 0:
            width = yellow // i
            height = i
            if 2*width + 2*height + 4 == brown:
                return [width + 2, height + 2]
def find_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append((i, n//i))
    return divisors

def solution(brown, yellow):
    for horiz, verti in find_divisors(yellow):
        if brown == (horiz + verti + 2) * 2:
            return [verti+2, horiz+2]
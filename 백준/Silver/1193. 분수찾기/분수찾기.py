n = int(input())
level = 1
while level < n:
    n -= level
    level += 1

if level%2 == 0:
    a = n
    b = level + 1 - n
    
else:
    a = level + 1 - n
    b = n

print(f'{a}/{b}')

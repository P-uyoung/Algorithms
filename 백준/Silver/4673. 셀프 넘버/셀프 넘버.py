made = set() 
ans = []
for i in range(1, 10001):
    if i not in made:
        made.add(i)
        ans.append(i)
    add = i
    for j in str(i):
        add += int(j)
    made.add(add)
print(*ans, sep='\n')
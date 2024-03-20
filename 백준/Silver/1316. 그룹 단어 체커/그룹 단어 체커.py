n = int(input())
count = 0
for _ in range(n):
    s = input()
    past = set(s[0])
    prev = s[0]
    for i,k in enumerate(s):
        if prev == k: continue
        elif k in past: 
            i -=1
            break
        past.add(k)
        prev = k
    if i == len(s)-1:
        count += 1
print(count)
        
           
    
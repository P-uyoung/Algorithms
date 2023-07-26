import re
s = input()
alphab = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
ans = 0
for a in alphab:
    ns = re.sub(a, ' ', s)
    if len(s) > len(ns):
        ans += ((len(s)-len(ns))//(len(a)-1))
        s = ns
s = re.sub(' ', '', s)
ans += len(s)
print(ans)
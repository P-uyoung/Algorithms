from collections import defaultdict
name = defaultdict(int)
for _ in range(int(input())):
    name[input()[0]] += 1
name = [k for k,v in sorted(name.items()) if v >=5]
if not name:
    print("PREDAJA")
else:
    print("".join(str(k) for k in name))
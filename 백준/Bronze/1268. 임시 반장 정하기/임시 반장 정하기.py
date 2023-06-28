from collections import Counter
from collections import defaultdict
n = int(input())
arr = [set() for _ in range(n)]

table = []
for _ in range(n):
    table.append(list(map(int, input().split())))

for x in range(5):
    gradeDict = defaultdict(list)
    for y in range(n):
        gradeDict[table[y][x]].append(y+1)
    keys = [k for k, v in gradeDict.items() if len(v)>= 2]
    for key in keys:
        v = gradeDict[key]
        for stu in v:
            for x in v:
                if x != stu:
                    arr[stu-1].add(x)

for i in range(n):
    arr[i] = len(arr[i])

print(arr.index(max(arr))+1)

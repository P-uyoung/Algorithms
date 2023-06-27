n, m = map(int, input().split())
arrN, arrM = set(), set()
for _ in range(n):
    arrN.add(input())
for _ in range(m):
    arrM.add(input())
    
res = list(arrN & arrM)
res.sort()
rN = len(res)
print(rN)
for i in range(rN):
    print(res[i])
               
    
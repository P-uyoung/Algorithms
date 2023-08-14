import sys
n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.sort(reverse=True)
ans = 0
for i, a in enumerate(arr):
   if a-i > 0:
       ans += (a-i)
sys.stdout.write(str(ans))
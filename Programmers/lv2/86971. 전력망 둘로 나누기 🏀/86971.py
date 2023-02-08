def solution(n, wires):
    ans = n
    for sub in (wires[i+1:] + wires[:i] for i in range(n)):     ## Good
        s = set(sub[0])
        [s.update(v) for _ in sub for v in sub if set(v) & s]
        ans = min(ans, abs(n-2*len(s)))
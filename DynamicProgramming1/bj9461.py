# 파도반 수열

import sys

T = int(input())
p = [0 for _ in range(100)]
p[0] = p[1] = p[2] = 1

def findP(n):
    if n > 3:
        for i in range(3, n):
            p[i] = p[i-2] + p[i-3]
        return p[n-1]
    else:
        return p[n-1]

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    print(findP(N))

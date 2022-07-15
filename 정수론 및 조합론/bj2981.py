# 검문.. 참고 사이트 및 반례
# https://gom20.tistory.com/164
# https://www.acmicpc.net/board/view/25895

import sys

def gcd(a, b):
    while b:
        tmp = a%b
        a = b
        b = tmp
    return a

N = int(input())
number = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
number.sort()
diffNumber = [number[i]-number[i-1] for i in range(1, N)]
GCD = []
divisor = []

if N == 2:
    GCD.append(number[1]-number[0])
else:
    for i in range(1, N-1):
        A = max(diffNumber[i], diffNumber[i-1])
        B = min(diffNumber[i], diffNumber[i-1])
        GCD.append(gcd(A, B))

div = min(GCD)
for k in range(1, int(div**(1/2))+1):
    if div%k == 0:
        divisor.append(k)
        if k != div//k:
            divisor.append(div//k)
#print(GCD)
divisor.sort()

print(*divisor[1:])
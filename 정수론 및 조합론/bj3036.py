# 링
# 최대공약수로 분모와 분자를 나누면 기약분수가 된다..<-이게 포인트인듯.

import sys

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

N = int(input())
radius = list(map(int, sys.stdin.readline().split()))

for i in radius[1:]:
    if radius[0]%i == 0:
        A = radius[0]//i
        B = 1
        print(f'{A}/{B}')
    else:
        GCD = gcd(radius[0], i)
        A = radius[0]//GCD
        B = i//GCD
        print(f'{A}/{B}')

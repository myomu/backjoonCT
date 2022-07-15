# 약수
import sys

N = int(input())
divisor = list(map(int, sys.stdin.readline().split()))
while True:
    if len(divisor) == 1:
        print(divisor[0]**2)
        break
    else:
        value = max(divisor) * min(divisor)
        print(value)
        break

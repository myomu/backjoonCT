# 하키
import sys

W, H, X, Y, P = map(int, sys.stdin.readline().split())
r = H/2
cnt = 0
for _ in range(P):
    x, y = map(int, sys.stdin.readline().split())
    case1 = (x-X)**2 + ((y-r-Y)**2) <= r**2
    case2 = (x-X-W)**2 + ((y-r-Y)**2) <= r**2
    case3 = (0 <= x-X <= W) and (0 <= y-Y <= H)
    if case1:
        cnt += 1
    elif case2:
        cnt += 1
    elif  case3:
        cnt += 1

print(cnt)
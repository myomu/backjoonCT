# 터렛

import sys, math

t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    distance = math.sqrt((abs(x1-x2)**2) + (abs(y1-y2)**2))

    if distance == 0 and r1 == r2:
        print(-1)
        continue

    if distance == abs(r1-r2) or distance == (r1+r2):
        print(1)
    elif abs(r1-r2) < distance < (r1+r2):
        print(2)
    elif distance > (r1+r2) or distance < abs(r1-r2):
        print(0)
    else:
        print('error')


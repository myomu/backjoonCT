# 어린 왕자
# 풀이 방식은 원의 공식을 이용한다. (x-cx)**2 + (y-cy)**2 = r**2
# r의 제곱보다 작으면 원 안에 좌표가 존재하는 것을 이용한다.
# 각 좌표가 해당 원 안에 있으면 출/입 이 한 번 발생하게 된다.
# 이때 출발점과 도착점의 위치를 잘 고려해야한다. 동시에 같은 원 안에 있을 경우..

import sys

T = int(input())
result = []
for _ in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    N = int(input())
    cnt = 0
    for i in range(N):
        cx, cy, r = map(int, sys.stdin.readline().split())
        case1 = (x1-cx)**2 + (y1-cy)**2 < r**2
        case2 = (x2-cx)**2 + (y2-cy)**2 < r**2
        if case1 and case2: # 이 부분 빼먹었을 때 틀렸다. 
            continue        # 출발점과 도착점이 한 원안에 있을 경우 통과해야할 원이 존재하지 않는다.
        if case1:
            cnt += 1
        if case2:
            cnt += 1
    result.append(cnt)

print(*result, sep='\n')
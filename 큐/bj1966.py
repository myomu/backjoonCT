# 프린터 큐
# 풀긴 풀었는데 코드가 너무 난잡한거 같다..;;

import sys
from collections import deque

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, l = map(int, input().split())
    li = deque(list(map(int, input().split())))    
    cnt = 0
    while len(li) > 0:
        maxValue = max(li)
        if l == -1:
            l = len(li)-1
        if li[0] == maxValue:
            li.popleft()
            cnt += 1
            if l == 0:
                break
            else:
                l -= 1          
        else:
            li.rotate(-1)
            l -= 1
    print(cnt)